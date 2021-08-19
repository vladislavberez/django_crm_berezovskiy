from django.contrib import admin
from catalog.models import Company, ContactPhones, ContactEmail, Connection, Project, User, Manager

# admin.site.register(Company)
# admin.site.register(ContactPhones)
# admin.site.register(ContactEmail)
# admin.site.register(Connection)
# admin.site.register(Project)
# admin.site.register(Manager)
# admin.site.register(User)

class ContactPhonesInLine(admin.TabularInline):
    model = ContactPhones
    extra = 0

class ContactEmailInLine(admin.TabularInline):
    model = ContactEmail
    extra = 0

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_company', 'full_name', 'created_at', 'address')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ContactPhonesInLine, ContactEmailInLine]

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name_manager', 'name_company')

@admin.register(ContactPhones)
class ContactPhonesAdmin(admin.ModelAdmin):
    list_display = ('name_manager', 'name_company', 'phone', 'status')

@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    list_display = ('name_manager', 'name_company', 'email', 'status')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name_project', 'company', 'start_date', 'deadline')

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('name_project', 'user', 'created_at')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions')
