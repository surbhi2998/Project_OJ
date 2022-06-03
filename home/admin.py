from django.contrib import admin
from .models import Items,User,Solutions,Problems,TestCases,Contact
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from home.views import User



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name','email', 'password', 'rank',
                  'isAdmin', 'is_staff', 'problemSolved')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('name','email', 'password', 'rank',
                  'isAdmin', 'is_staff', 'problemSolved')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name','email', 'password', 'rank',
                  'isAdmin', 'is_staff', 'problemSolved')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','rank','isAdmin','problemSolved')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'rank','name', 'password1', 'password2','problemSolved')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

@admin.register(User)
class AdminUser(UserAdmin):
    pass

# Register your models here.
# class ItemsAdmin(admin.ModelAdmin):
#     pass
# class UserAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Items,ItemsAdmin)
# admin.site.register(User,UserAdmin)
@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    pass
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
@admin.register(Solutions)
class SolutionsAdmin(admin.ModelAdmin):
    pass
@admin.register(Problems)
class ProblemsAdmin(admin.ModelAdmin):
    pass
@admin.register(TestCases)
class TestCaseAdmin(admin.ModelAdmin):
    pass
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


# Register your models here.
