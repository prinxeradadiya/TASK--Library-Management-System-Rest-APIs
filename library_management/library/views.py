from rest_framework import viewsets
from .models import Book, Member, Loan
from .serializers import BookSerializer, MemberSerializer, LoanSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import date

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    @action(detail=False, methods=['post'])
    def borrow(self, request):
        book_id = request.data.get('book_id')
        member_id = request.data.get('member_id')
        due_date = request.data.get('due_date')

        # Business logic
        book = Book.objects.get(id=book_id)
        if book.copies_available < 1:
            return Response({'error': 'No copies available'}, status=400)

        member = Member.objects.get(id=member_id)
        loan = Loan.objects.create(book=book, member=member, due_date=due_date)
        book.copies_available -= 1
        book.save()
        return Response({'message': 'Book borrowed successfully'})

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        loan = self.get_object()
        loan.return_date = date.today()
        days_overdue = (loan.return_date - loan.due_date).days
        if days_overdue > 0:
            loan.fine = days_overdue * 10  # Example fine calculation
        loan.save()

        # Update book copies
        book = loan.book
        book.copies_available += 1
        book.save()

        return Response({'message': 'Book returned successfully'})
