
class CWRTransmissionHeader:
	"""
		The transmission header record is the first record object 
		required in any CWR file. It contains basic metadata 
		about all of the data contained within the file
	"""
	record_type = 'HDR'
	
	sender_types = (
		'PB', # Publisher
		'SO', # Society
		'AA', # Administrative Agency
		'WR' # Writer
	)

	EDI_standard = '01.10'
	
	def __init__(
		self, 
		record_type: str = record_type, 
		sender_type: str, 
		sender_id: int, 
		sender_name: str
		)



class CWRFile:
	def __init__(self, version, file_name, sender, works):
		self.version = version
		self.file_name = file_name
		self.sender = sender
		self.works = works


	def render(self, file_path=None):
		_file = ''.join(file_path, self.file_name)
		with open(_file, 'w', 'ascii') as cwr_file:
