from django.db import models


class Languages(models.Model):
    language = models.CharField(
        max_length=100, unique=True, null=False, blank=False
    )
    language_code = models.CharField(
        max_length=100, unique=True,  null=False, blank=False
    )

    def __str__(self):
        return str(self.language)

    class Meta:
        verbose_name_plural = 'Languages'
        verbose_name = 'Language'


class Quotes(models.Model):
    quote = models.TextField(
        verbose_name='Literary Quote',
        null=False,
        blank=False,
        unique=True
    )
    book = models.CharField(
        max_length=300, verbose_name='Book', default='Nonexistent.'
    )
    author = models.CharField(
        max_length=300, verbose_name='Author', default='Nonexistent.'
    )
    language = models.ForeignKey(
        Languages, null=True, blank=False, on_delete=models.CASCADE
    )

    def __str__(self):
        if len(self.quote) > 30:
            cutted_quote = str(self.quote)[0:29]

            if cutted_quote[-1] == '.':
                cutted_quote = cutted_quote[0: -1]

            return f'{cutted_quote.strip()}... - {str(self.author)}'

        return f'{str(self.quote)} - {str(self.author)}'

    class Meta:
        verbose_name_plural = 'Quotes'
        verbose_name = 'Quote'
