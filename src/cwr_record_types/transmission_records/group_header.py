from base_fields import AlphanumericField, NumericField, ListTableLookupField

class RecordType(AlphanumericField):
	'''
	'''
	def __init__(self):
		self.start = 1
		self.size = 3
		self.required = 'M' #Mandatory
		self.value = 'GRH'
		super()


class TransactionType(ListTableLookupField):
	'''
	'''
	def __init__(self):
		self.start = 4
		self.size = 3
		self.required = 'M' #Mandatory
		super()


class GroupID(NumericField):
	'''
	A unique sequential number for this group within this file.
	Group ID should start at 00001.
	'''
	default = 1
	def __init__(self, value):
		self.start = 7
		self.size = 5
		self.required = 'M' #Mandatory
		self.value = value
		super()


class TransactionTypeVersionNumber(AlphanumericField):
	'''
	'''
	def __init__(self):
		self.start = 12
		self.size = 5
		self.required = 'M' #Mandatory
		self.value = '02.10'
		super()


class BatchRequest(NumericField):
	'''
	A unique sequential number to identify the group. This number is managed 
	by the submitter to identify the group among multiple submission files.
	'''
	default = 1
	def __init__(self, value=None):
		self.start = 17
		self.size = 10
		self.required = 'O' #Optional
		self.value = value if value else BatchRequest.default
		super()


class SubmissionType(ListTableLookupField):
	'''
	Set to blank - Not used for CWR
	'''
	def __init__(self):
		self.required = 'C' #Conditional
		super()


class GroupHeader:
	'''
	The GRH record is used to indicate the presence of a group (or batch) 
	of transactions within the file. A group can only contain one type of 
	transaction and this is indicated in the Transaction Type field. Also 
	all transactions of the same type should be contained in the same group 
	(e.g. all NWR transactions should appear in one single NWR group) and each 
	group type can only be used once per file (i.e. there can only be one NWR 
	and one REV group per file)
	'''
	def __init__(self, transaction_type, group_id=GroupID.default, batch_request=None):
		self.record_type = RecordType()
		self.transaction_type = TransactionType(transaction_type)
		self.group_id = GroupID(group_id)
		self.TransactionTypeVersionNumber = TransactionTypeVersionNumber()
		self.batch_request = BatchRequest(batch_request)