from base_fields import AlphanumericField, NumericField, ListTableLookupField


class RecordType(AlphanumericField):
	'''
	GRT = Group Trailer
	'''
	def __init__(self):
		self.start = 1
		self.size = 3
		self.required = 'M' #Mandatory
		self.value = 'GRT'
		super()


class GroupID(NumericField):
	'''
	The same group id that was present on the preceding GRH
	record.
	'''
	def __init__(self, value):
		self.start = 4
		self.size = 5
		self.required = 'M' #Mandatory
		self.value = value


class TransactionCount(NumericField):
	'''
	The number of transactions included within this group.
	'''
	def __init__(self, value):
		self.start = 9
		self.size = 8
		self.required = 'M' #Mandatory
		self.value = value


class RecordCount(NumericField):
	'''
	The number of physical records included within this group
	including GRH and GRT records
	'''
	def __init__(self, value):
		self.start = 17
		self.size = 8
		self.required = 'M' #Mandatory


class GroupTrailer
	'''
	The Group Trailer Record indicates the end of a group and 
	provides both transaction and record counts for the group
	'''
	def __init__(self, group_id, transaction_count, record_count):
		self.record_type = RecordType()
		self.group_id = group_id
		self.transaction_count = TransactionCount(transaction_count)
		self.record_count = RecordCount(record_count)
