
class RecordPrefix(AlphaNumericField):
	'''
	Set Record Type = NWR (New Work Registration) for new
	registrations, REV (Revised Registration) for revisions, or
	ISW (Notification of ISWC) or EXC (Existing Work in
	Conflict) for outgoing notifications.
	'''
	prefix_options = (
		'NWR', #New Work Registratioin
		'REV'  #Revised Worrk Registration
	)

	def __init__(self, prefix_type : str = 'NWR'):
		self.start = 1
		self.size = 19
		self.required = 'M' #Mandatory
		self.prefix_type = prefix_type
		super()

		if self.prefix_type not in self.available_prefix_types:
			valids = ', '.join(self.prefix_options)
			raise ValueError(
				f'invalid transaction header type. must be one of {valids}'
			)


class WorkTitle(AlphaNumericField):
	'''
	Name/Title of the work.
	'''
	def __init__(self, value):
		self.start = 20
		self.size = 60
		self.required = 'M' #Mandatory
		self.value = value
		super()


class LanguageCode(ListTableLookupField):
	'''
	The code representing the language of this title. These
	values reside in the Language Code Table.
	'''
	default = None
	def __init__(self, value):
		self.start = 80
		self.size = 2
		self.required = 'O' #Optional
		self.value = value
		super()


class SubmitterWorkNumber(AlphaNumericField):
	'''
	Number assigned to the work by the publisher submitting
	or receiving the file. This number must be unique for the
	publisher.
	'''
	def __init__(self, value):
		self.start = 82
		self.size = 14
		self.required = 'M' #Mandatory
		self.value = value


class ISWC(AlphaNumericField):
	'''
	The International Standard Work Code assigned to this work.
	'''
	def __init__(self, value):
		self.start = 96
		self.size = 11
		self.required = 'O' #Optional
		self.value = value


class CopyrightDate(DateField):
	'''
	Original copyright date of the work.
	'''
	default = None
	def __init__(self, value):
		self.start = 107
		self.size = 8
		self.required = 'O' #Optional
		self.value = value


class CopyrightNumber(AlphaNumericField)
	'''
	Original copyright number of the work.
	'''
	default = None
	def __init__(self, value):
		self.start = 115
		self.size = 12
		self.required = 'O' #Optional
		self.value = value


class MusicalWorkDistribution(ListTableLookupField):
	'''
	Describes the type of music as it applies to special
	distribution rules. Values for this field reside in the Musical
	Work Distribution Category Table.
	'''
	def __init__(self, value):
		self.start = 127
		self.size = 3
		self.required = 'M' #Mandatory
		self.value = value


class CategoryDuration(TimeDurationField):
	'''
	Duration of the work in hours, minutes, and seconds. This
	field must be greater than zero if Musical Work
	Distribution Category is equal to SER. Note that some
	societies may also require duration for works where the
	Musical Work Distribution Category is equal to JAZ (e.g.
	BMI).
	'''
	def __init__(self, value):
		self.start = 130
		self.size = 6
		self.required = 'C' #Conditional
		self.value = value


class RecordedIndicator(FlagField):
	'''
	Indicates whether or not the work has ever been recorded.
	'''
	def __init__(self, value):
		self.start = 136
		self.size = 1
		self.required = 'M' #Mandatory
		self.value = value


class TextMusicRelationship(ListTableLookupField):
	'''
	Indicates whether this work contains music, text, and/or
	both. Values reside in the Text Music Relationship Table.
	'''
	default = None
	def __init__(self, value):
		self.start = 137
		self.size = 3
		self.required = 'O' #Optional
		self.value = value


class CompositeType(ListTableLookupField):
	'''
	If this is a composite work, this field will indicate the type
	of composite. Values reside in the Composite Type Table.
	'''
	default = None
	def __init__(self, value):
		self.start = 140
		self.size = 3
		self.required = 'O' #Optional
		self.value = value


class VersionType(ListTableLookupField):
	'''
	Indicates relationships between this work and other
	works. Note that this field is used to indicate whether or
	not this work is an arrangement. Values reside in the
	Version Type Table
	'''
	def __init__(self, value):
		self.start = 143
		self.size = 3
		self.required = 'M' #Mandatory
		self.value = value


class ExcerptType(ListTableLookupField):
	'''
	If this is an excerpt, this field will indicate the type of
	excerpt. Values reside in the Excerpt Type Table.
	'''
	default = None
	def __init__(self, value):
		self.start = 146
		self.size = 3
		self.required = 'O' #Optional
		self.value = value


class MusicArrangement(ListTableLookupField):
	'''
	If Version Type is equal to “MOD”, this field indicates the
	type of music arrangement. Values reside in the Music
	Arrangement Table.
	'''
	def __init__(self, value):
		self.start = 149
		self.size = 3
		self.required = 'C' #Conditional
		self.value = value


class LyricAdaption(ListTableLookupField):
	'''
	If Version Type is equal to “MOD”, this field indicates the
	type of lyric adaptation. Values reside in the Lyric
	Adaptation Table.
	'''
	def __init__(self, value):
		self.start = 152
		self.size = 3
		self.required = 'C' #Conditional
		self.value = value


class ContactName(AlphaNumericField):
	'''
	The name of a business contact person at the organization
	that originated this transaction.
	'''
	default = None
	def __init__(self, value):
		self.start = 155
		self.size = 30
		self.required = 'O' #Optional
		self.value = value


class ContactID(AlphaNumericField):
	'''
	An identifier associated with the contact person at the
	organization that originated this transaction.
	'''
	default = None
	def __init__(self, value):
		self.start = 185
		self.size = 10
		self.required = 'O' #Optional
		self.value = value


class CWRWorkType(ListTableLookupField):
	'''
	These values reside in the CWR Work Type table.
	'''
	default = None
	def __init__(self, value):
		self.start = 195
		self.size = 2
		self.required = 'O' #Optional
		self.value = value


class GrandRightsIndicator(BooleanField):
	'''
	Indicates whether this work is originally intended for
	performance on stage.
	Note that this field is mandatory for registrations with the
	UK societies.
	'''
	def __init__(self, value):
		self.start = 197
		self.size = 1
		self.required = 'C' #Conditional
		self.value = value


class CompositeComponentCount(NumericField):
	'''
	If Composite Type is entered, this field represents the
	number of components contained in this composite.
	Note that this is required for composite works where
	ASCAP is represented on the work.
	'''
	default = 0
	def __init__(self, value):
		self.start = 198
		self.size = 3
		self.required = 'C' #Conditional
		self.value = value


class WorkRegistrationTransaction(Transaction):
	def __init__(
			self, 
			reg_type=None, 
			work_title, 
			language='EN', 
			submitter_work_number,
			iswc,
			copyright_date=CopyrightDate.default,
			copyright_number=copyright_number.default,
			musical_work_distribution=MusicalWorkDistribution.default,
			category_duration=CategoryDuration.default,
			recorded_indidcator,
			text_music_relationship=TextMusicRelationship.default,
			composite_type=CompositeType.default,
			version_type,
			excerpt_type=ExcerptType.default,
			music_arrangement=MusicArrangement.default,
			lyric_adaption=LyricAdaption.default,
			contact_name=ContactName.default,
			contact_id=ContactID.default,
			cwr_work_type=CWRWorkType.default,
			grand_rights_indicator=GrandRightsIndicator.default,
			composite_component_count=CompositeComponentCount.default
			):
		self.record_prefix = RecordPrefix(reg_type)
		self.work_title = WorkTitle(work_title)
		self.language = LanguageCode(language)
		self.submitter_work_number = SubmitterWorkNumber(submitter_work_number)
		self.iswc = ISWC(iswc)
		self.copyright_date = CopyrightDate(copyright_date)
		self.copyright_number = CopyrightNumber(copyright_number)
		self.musical_work_distribution = MusicalWorkDistribution(musical_work_distribution)
		self.category_duration = CategoryDuration(category_duration)
		self.recorded_indidcator = RecordedIndicator(recorded_indidcator)
		self.text_music_relationship = TextMusicRelationship(text_music_relationship)
		self.composite_type = CompositeType(composite_type)
		self.version_type = VersionType(version_type)
		self.excerpt_type = ExcerptType(excerpt_type)
		self.music_arrangement = MusicArrangement(music_arrangement)
		self.lyric_adaption = LyricAdaption(lyric_adaption)
		self.contact_name = ContactName(contact_name)
		self.contact_id = ContactID(contact_id)
		self.cwr_work_type = CWRWorkType(cwr_work_type)
		self.grand_rights_indicator = GrandRightsIndicator(grand_rights_indicator)
		self.composite_component_count = CompositeComponentCount(composite_component_count)

		#Header - NWR, REV, ISW, EXC
		#Publisher Controlled By Submitter - SPU
		#Publisher Territory of Control - SPT
