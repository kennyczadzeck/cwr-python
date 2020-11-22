from datetime import datetime

class DataElement:
	'''
	'''
	format_types = Set(
		'A', # Alphanumeric
		'B', # Boolean
		'F', # Flag
		'D', # Date
		'N', # Numeric
		'T', # Time or Duration
		'L'  # List or Table Lookup
	)

	required_statuses = Set(
		'M', # Mandatory
		'C', # Conditional
		'O'  # Optional
	)


	def __init__(self, start : int, size : int, format_type : str, required: str):
		self.start = start
		self.size = size
		self.format_type = format_type
		self.required = required

		if self.format_type not in self.format_types:
			valids = ', '.join(self.format_types)
			raise ValueError(
				f'format type of {self.field_name} is invalid. must be in {valids}'
			)
		if self.required not in self.required_statuses:
			valids = ', '.join(self.required_statuses)
			raise ValueError(
				f'required status of {self.field_name} is invalid. must be in {valids}'
			)


	@property
	def field_name(self):
		return self.__name__


class NumericField(DataElement):
	'''
	'''
	def __init__(self, value):
		self.format_type : str = 'N'
		self.value : int
		self.decimal : int = 0
		super()


	def _right_justify_val_as_str(self):
		val_as_string = str(self.value)
		delta = len(val_as_string) - self.size
		if delta:
			for position in range(1, delta):
				val_as_string = '0' + val_as_string
		self._val_as_str = val_as_string


	def __str__(self) -> str:
		if not hasattr(self, '_val_as_str'):
			self._right_justify_val_as_str()
		return self._val_as_str


class AlphanumericField(DataElement):
	'''
	'''
	encoding = 'ascii'

	def __init__(self, value):
		self.format_type = 'A'
		self.value = value

		try:
			self.value.decode(self.encoding)
		except: UnicodeError(
			f'value {self.value} provided to {self.field} is not in {self.encoding}'
		)

		super()


class BooleanField(DataElement):
	'''
	'''
	def __init__(self, value : bool):
		self.format_type = 'B'
		self.size = 1
		self.value = value
		super()


	def __str__(self) -> str:
		return 'Y' if self.value is True else 'N'


class FlagField(DataElement):
	'''
	'''
	flag_types = ('Y', 'N', 'U')

	def __init__(self, value : str):
		self.format_type = 'F'
		self.size = 1
		self.value = value.upper()

		if self.value not in self.flag_types:
			raise ValueError(
				f'flag type of {self.field} is invalid. must be in {self.flag_types}'
			)


class DateField(DataElement):
	'''
	'''
	date_format = '%Y%m%d' #YYYYMMDD

	def __init__(self, value=datetime.date.today()):
		self.format_type = 'D'
		self.size = 8
		self.value = value.strftime(self.date_format)
		super()


class TimeDurationField(DataElement):
	'''
	'''
	time_format = '%H%M%S' #HHMMSS

	def __init__(self, value=datetime.utcnow()):
		self.format_type = 'T'
		self.size = 6
		self.value = value.strftime(self.time_format)
		super()


class ListTableLookupField(DataElement):
	'''
	'''
	def __init__(self):
		self.format_type = 'L'
		super()
