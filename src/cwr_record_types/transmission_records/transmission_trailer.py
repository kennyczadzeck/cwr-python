from base_fields import AlphanumericField, NumericField


class RecordType(AlphanumericField):
	'''
	'''
	def __init__(self):
		self.start = 1
		self.size = 3
		self.required = 'M' #Mandatory
		self.value = 'TRL'
		super()


class GroupCount(NumericField):
	'''
	'''
	def __init__(self, value):
		self.start = 4
		self.size = 5
		self.required = 'M' #Mandatory
		self.value = value
		super()


class TransactionCount(NumericField):
	'''
	'''
	def __init__(self, value):
		self.start = 9
		self.size = 8
		self.required = 'M' #Mandatory
		self.value = value
		super()


class RecordCount(NumericField):
	'''
	'''
	def __init__(self, value):
		self.start = 17
		self.size = 8
		self.required = 'M' #Mandatory
		self.value = value
		super()


class TransmissionTrailer:
	'''
	The Transmission Trailer record indicates the end of the transmission 
	file. Control totals representing the number of groups, transactions, 
	and records within the file are included on this record.
	'''
	def __init__(self, group_count, transaction_count, record_count):
		self.record_type = RecordType()
		self.group_count = GroupCount(group_count)
		self.transaction_count = TransactionCount(transaction_count)
		self.record_count = RecordCount(record_count)