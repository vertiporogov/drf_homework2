from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    """Команда для первоначального заполнения БД данными из json-файла"""
    def handle(self, *args, **options):
        call_command('loaddata', 'payments_data.json')