from base_fields import AlphanumericField, NumericField, DateField, TimeDurationField


class RecordType(AlphanumericField):
	'''
	'''
	def __init__(self):
		self.start = 1
		self.size = 3
		self.required = 'M' #Mandatory
		self.value = 'HDR' #Transmission Header
		super()


class SenderType(AlphanumericField):
	'''
	'''
	sender_types = (
		'PB', # Publisher
		'SO', # Society
		'AA', # Administrative Agency
		'WR' # Writer
	)

	def __init__(self, value):
		self.start = 4
		self.size = 2
		self.required = 'M' #Mandatory
		self.value = value

		if self.value not in self.sender_types:
			valids = ', '.join(self.sender_types)
			raise ValueError(f'HDR sender type needs to be one of {valids}')


class SenderID(NumericField):
	'''
	'''
	def __init__(self, value):
		self.start = 6
		self.size = 9
		self.required = 'M' #Mandatory
		self.value = value
		super()


class SenderName(AlphanumericField):
	'''
	'''
	def __init__(self):
		self.start = 15
		self.size = 45
		self.required = 'M' #Mandatory
		super()


class EDIStandardVersionNumber(AlphanumericField):
	'''
	'''
	def __init__(self, value='01.10'):
		self.start = 60
		self.size = 5
		self.required = 'M' #Mandatory
		self.value = value


class CreationDate(DateField):
	'''
	'''
	def __init__(self, value=None):
		self.start = 65
		self.size = 8
		self.required = 'M' #Mandatory
		if value:
			self.value = value
		super()


class CreationTime(TimeDurationField):
	'''
	'''
	def __init__(self, value=None):
		self.start = 73
		self.size = 6
		self.required = 'M' #Mandatory
		if value:
			self.value = value
		super()


class TransmissionDate(DateField):
	'''
	'''
	def __init__(self, value=None):
		self.start = 79
		self.size = 8
		self.required = 'M' #Mandatory
		if value:
			self.value = value
		super()


class TransmissionHeader:
	"""
		This is a required “cover sheet” for transmissions submitted by a 
		participant. It will contain the file control information as well as 
		the name of the submitter.
		
		The character set field added for Version 2.1 is simply intended to be 
		a way of informing societies that there is a non-ASCII character set 
		(such as Chinese Characters) used somewhere in the file. Such files are 
		only intended to be sent to societies that accept and use such character 
		sets (e.g. CASH), and the value in the field will inform those societies 
		which character set has been used. The list of the relevant character 
		sets is currently being developed and will appear in the lookup tables 
		once it is ready. If such a file is sent to a society that does not 
		accept non-ASCII characters then it should get rejected in the normal 
		way during the file validation process.

		If a publisher must send a CWR Sender ID (IPNN) greater than 9 digits, 
		then as a workaround the submitting publisher can use the existing 
		Sender Type field to provide the leading two numbers of the CWR Sender 
		ID (IPNN) and use the existing Sender ID field to provide the remaining 
		9 digits (2 + 9 = 11 Digits). This potential workaround should be 
		discussed between the submitting publisher and the receiving societies 
		prior implementation since the receiving societies will have to accept 
		a numeric value in place of the Sender Type and concatenate the Sender 
		Type and Sender ID fields to render the 11 CWR Sender ID (IPNN).
	"""
	def __init__(
			self, 
			sender_type, 
			sender_id, 
			sender_name,
			creation_date = CreationDate(),
			creation_time = CreationTime(),
			transmission_date = TransmissionDate()
			):
		self.record_type = RecordType()
		self.sender_type = SenderType(sender_type)
		self.sender_id = SenderID(sender_id)
		self.sender_name = SenderName(sender_name)
		self.creation_date = creation_date
		self.creation_time = creation_time
		self.transmission_date = transmission_date