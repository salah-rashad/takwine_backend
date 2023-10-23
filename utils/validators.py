from django.forms import ValidationError


class FileSizeValidator(object):
    max_size: int

    def __init__(self, max_size: int = 2):
        """Validates the size of the file.

        Args:
            max_size (int, optional): is the maximum size allowed in megabytes. Defaults to 2.
        """
        self.max_size = max_size

    def __call__(self, value):
        limit = self.max_size * 1024 * 1024  # converting to bytes
        if value.size > limit:
            raise ValidationError('الملف كبير. يجب أن لا يتعدى حجم الملف {} MB.'.format(self.max_size))
