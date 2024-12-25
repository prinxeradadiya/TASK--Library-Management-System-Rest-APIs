
from django.contrib import admin
from .models import Book, Member, Loan

# Register Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'copies_available')  # Display columns in admin
    search_fields = ('title', 'author', 'genre')  # Enable search
    list_filter = ('genre',)  # Add filters by genre

# Register Member
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')  # Display columns in admin
    search_fields = ('name', 'email')  # Enable search

# Register Loan
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'member', 'loan_date', 'due_date', 'return_date', 'fine')
    search_fields = ('book__title', 'member__name')  # Enable search by related fields
    list_filter = ('loan_date', 'due_date', 'return_date')  # Add date filters
