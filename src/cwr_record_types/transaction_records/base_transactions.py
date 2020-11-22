

class Transaction:
	def __init__(self, header_record, detail_records):
		self.header = header_record
		self.detail_records = detail_records