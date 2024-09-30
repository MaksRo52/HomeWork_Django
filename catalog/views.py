from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.views import generic
from django.urls import reverse_lazy
from catalog.forms import ProductForm, VersionForm, CategoryForm, ModeratorForm
from catalog.models import Product, Category, Version
from catalog.services import get_product_from_cache, get_category_from_cache


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data["object_list"]:
            active_version = Version.objects.filter(
                product=product, active=True
            ).first()
            product.active_version = active_version
        return context_data

    def get_queryset(self):
        return get_product_from_cache()


class ContactsView(generic.TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Product


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        Version.objects.create(product=product, active=True)
        user = self.request.user
        product.autor = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context["formset"] = ProductFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object  # set the Product instance to the formset
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    def get_form_class(self):
        user = self.request.user
        if user == self.object.autor:
            return ProductForm
        elif (
            user.has_perm("catalog.edit_description")
            and user.has_perm("catalog.set_published")
            and user.has_perm("catalog.edit_category")
        ):
            return ModeratorForm
        raise PermissionDenied


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Category
    form_class = CategoryForm


class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Category
    form_class = CategoryForm


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Product
    success_url = reverse_lazy("catalog:home")


class VersionCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Version
    form_class = VersionForm


class CategoryListView(generic.ListView):
    model = Category

    def get_queryset(self):
        return get_category_from_cache()
