# Generated by Django 2.2.24 on 2021-12-25 02:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import judge.models.problem
import judge.models.profile


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0121_per_problem_sub_access_control'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestproblem',
            options={'ordering': ('order',), 'verbose_name': 'contest problem', 'verbose_name_plural': 'contest problems'},
        ),
        migrations.AlterModelOptions(
            name='webauthncredential',
            options={'verbose_name': 'WebAuthn credential', 'verbose_name_plural': 'WebAuthn credentials'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='contest',
            name='format_name',
            field=models.CharField(choices=[('atcoder', 'AtCoder'), ('default', 'Default'), ('ecoo', 'ECOO'), ('icpc', 'ICPC'), ('ioi', 'IOI (pre-2016)'), ('ioi16', 'IOI')], default='default', help_text='The contest format module to use.', max_length=32, verbose_name='contest format'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='auth_key',
            field=models.CharField(help_text='A key to authenticate this judge', max_length=100, verbose_name='authentication key'),
        ),
        migrations.AlterField(
            model_name='language',
            name='description',
            field=models.TextField(blank=True, help_text='Use this field to inform users of quirks with your environment, additional restrictions, etc.', verbose_name='language description'),
        ),
        migrations.AlterField(
            model_name='languagelimit',
            name='memory_limit',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1048576)], verbose_name='memory limit'),
        ),
        migrations.AlterField(
            model_name='languagelimit',
            name='time_limit',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)], verbose_name='time limit'),
        ),
        migrations.AlterField(
            model_name='navigationbar',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='navigationbar',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='navigationbar',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='problem',
            name='allowed_languages',
            field=models.ManyToManyField(help_text='List of allowed submission languages.', to='judge.Language', verbose_name='allowed languages'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='authors',
            field=models.ManyToManyField(blank=True, help_text='These users will be able to edit the problem, and be listed as authors.', related_name='authored_problems', to='judge.Profile', verbose_name='creators'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='code',
            field=models.CharField(help_text='A short, unique code for the problem, used in the url after /problem/', max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[a-z0-9]+$', 'Problem code must be ^[a-z0-9]+$')], verbose_name='problem code'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='curators',
            field=models.ManyToManyField(blank=True, help_text='These users will be able to edit the problem, but not be listed as authors.', related_name='curated_problems', to='judge.Profile', verbose_name='curators'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(validators=[judge.models.problem.disallowed_characters_validator], verbose_name='problem body'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='group',
            field=models.ForeignKey(help_text='The group of problem, shown under Category in the problem list.', on_delete=django.db.models.deletion.CASCADE, to='judge.ProblemGroup', verbose_name='problem group'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='is_manually_managed',
            field=models.BooleanField(db_index=True, default=False, help_text='Whether judges should be allowed to manage data or not.', verbose_name='manually managed'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='license',
            field=models.ForeignKey(blank=True, help_text='The license under which this problem is published.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='judge.License'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='memory_limit',
            field=models.PositiveIntegerField(help_text='The memory limit for this problem, in kilobytes (e.g. 64mb = 65536 kilobytes).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1048576)], verbose_name='memory limit'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='name',
            field=models.CharField(db_index=True, help_text='The full name of the problem, as shown in the problem list.', max_length=100, verbose_name='problem name'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='points',
            field=models.FloatField(help_text="Points awarded for problem completion. Points are displayed with a 'p' suffix if partial.", validators=[django.core.validators.MinValueValidator(0)], verbose_name='points'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='testers',
            field=models.ManyToManyField(blank=True, help_text='These users will be able to view the private problem, but not edit it.', related_name='tested_problems', to='judge.Profile', verbose_name='testers'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='time_limit',
            field=models.FloatField(help_text='The time limit for this problem, in seconds. Fractional seconds (e.g. 1.5) are supported.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)], verbose_name='time limit'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='types',
            field=models.ManyToManyField(help_text="The type of problem, as shown on the problem's page.", to='judge.ProblemType', verbose_name='problem types'),
        ),
        migrations.AlterField(
            model_name='problemdata',
            name='checker',
            field=models.CharField(blank=True, choices=[('standard', 'Standard'), ('bridged', 'Custom checker'), ('floats', 'Floats'), ('floatsabs', 'Floats (absolute)'), ('floatsrel', 'Floats (relative)'), ('rstripped', 'Non-trailing spaces'), ('sorted', 'Unordered'), ('identical', 'Byte identical'), ('linecount', 'Line-by-line')], max_length=10, verbose_name='checker'),
        ),
        migrations.AlterField(
            model_name='problemtestcase',
            name='checker',
            field=models.CharField(blank=True, choices=[('standard', 'Standard'), ('bridged', 'Custom checker'), ('floats', 'Floats'), ('floatsabs', 'Floats (absolute)'), ('floatsrel', 'Floats (relative)'), ('rstripped', 'Non-trailing spaces'), ('sorted', 'Unordered'), ('identical', 'Byte identical'), ('linecount', 'Line-by-line')], max_length=10, verbose_name='checker'),
        ),
        migrations.AlterField(
            model_name='problemtranslation',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('vi', 'Vietnamese')], max_length=7, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_totp_enabled',
            field=models.BooleanField(default=False, help_text='check to enable TOTP-based two-factor authentication', verbose_name='TOTP 2FA enabled'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='scratch_codes',
            field=judge.models.profile.EncryptedNullCharField(blank=True, help_text='JSON array of 16 character base32-encoded codes                                                         for scratch codes', max_length=255, null=True, validators=[django.core.validators.RegexValidator('^(\\[\\])?$|^\\[("[A-Z0-9]{16}", *)*"[A-Z0-9]{16}"\\]$', 'Scratch codes must be empty or a JSON array of                                                                  16-character base32 codes')], verbose_name='scratch codes'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timezone',
            field=models.CharField(choices=[('Africa', [('Africa/Abidjan', 'Abidjan'), ('Africa/Accra', 'Accra'), ('Africa/Addis_Ababa', 'Addis_Ababa'), ('Africa/Algiers', 'Algiers'), ('Africa/Asmara', 'Asmara'), ('Africa/Asmera', 'Asmera'), ('Africa/Bamako', 'Bamako'), ('Africa/Bangui', 'Bangui'), ('Africa/Banjul', 'Banjul'), ('Africa/Bissau', 'Bissau'), ('Africa/Blantyre', 'Blantyre'), ('Africa/Brazzaville', 'Brazzaville'), ('Africa/Bujumbura', 'Bujumbura'), ('Africa/Cairo', 'Cairo'), ('Africa/Casablanca', 'Casablanca'), ('Africa/Ceuta', 'Ceuta'), ('Africa/Conakry', 'Conakry'), ('Africa/Dakar', 'Dakar'), ('Africa/Dar_es_Salaam', 'Dar_es_Salaam'), ('Africa/Djibouti', 'Djibouti'), ('Africa/Douala', 'Douala'), ('Africa/El_Aaiun', 'El_Aaiun'), ('Africa/Freetown', 'Freetown'), ('Africa/Gaborone', 'Gaborone'), ('Africa/Harare', 'Harare'), ('Africa/Johannesburg', 'Johannesburg'), ('Africa/Juba', 'Juba'), ('Africa/Kampala', 'Kampala'), ('Africa/Khartoum', 'Khartoum'), ('Africa/Kigali', 'Kigali'), ('Africa/Kinshasa', 'Kinshasa'), ('Africa/Lagos', 'Lagos'), ('Africa/Libreville', 'Libreville'), ('Africa/Lome', 'Lome'), ('Africa/Luanda', 'Luanda'), ('Africa/Lubumbashi', 'Lubumbashi'), ('Africa/Lusaka', 'Lusaka'), ('Africa/Malabo', 'Malabo'), ('Africa/Maputo', 'Maputo'), ('Africa/Maseru', 'Maseru'), ('Africa/Mbabane', 'Mbabane'), ('Africa/Mogadishu', 'Mogadishu'), ('Africa/Monrovia', 'Monrovia'), ('Africa/Nairobi', 'Nairobi'), ('Africa/Ndjamena', 'Ndjamena'), ('Africa/Niamey', 'Niamey'), ('Africa/Nouakchott', 'Nouakchott'), ('Africa/Ouagadougou', 'Ouagadougou'), ('Africa/Porto-Novo', 'Porto-Novo'), ('Africa/Sao_Tome', 'Sao_Tome'), ('Africa/Timbuktu', 'Timbuktu'), ('Africa/Tripoli', 'Tripoli'), ('Africa/Tunis', 'Tunis'), ('Africa/Windhoek', 'Windhoek')]), ('America', [('America/Adak', 'Adak'), ('America/Anchorage', 'Anchorage'), ('America/Anguilla', 'Anguilla'), ('America/Antigua', 'Antigua'), ('America/Araguaina', 'Araguaina'), ('America/Argentina/Buenos_Aires', 'Argentina/Buenos_Aires'), ('America/Argentina/Catamarca', 'Argentina/Catamarca'), ('America/Argentina/ComodRivadavia', 'Argentina/ComodRivadavia'), ('America/Argentina/Cordoba', 'Argentina/Cordoba'), ('America/Argentina/Jujuy', 'Argentina/Jujuy'), ('America/Argentina/La_Rioja', 'Argentina/La_Rioja'), ('America/Argentina/Mendoza', 'Argentina/Mendoza'), ('America/Argentina/Rio_Gallegos', 'Argentina/Rio_Gallegos'), ('America/Argentina/Salta', 'Argentina/Salta'), ('America/Argentina/San_Juan', 'Argentina/San_Juan'), ('America/Argentina/San_Luis', 'Argentina/San_Luis'), ('America/Argentina/Tucuman', 'Argentina/Tucuman'), ('America/Argentina/Ushuaia', 'Argentina/Ushuaia'), ('America/Aruba', 'Aruba'), ('America/Asuncion', 'Asuncion'), ('America/Atikokan', 'Atikokan'), ('America/Atka', 'Atka'), ('America/Bahia', 'Bahia'), ('America/Bahia_Banderas', 'Bahia_Banderas'), ('America/Barbados', 'Barbados'), ('America/Belem', 'Belem'), ('America/Belize', 'Belize'), ('America/Blanc-Sablon', 'Blanc-Sablon'), ('America/Boa_Vista', 'Boa_Vista'), ('America/Bogota', 'Bogota'), ('America/Boise', 'Boise'), ('America/Buenos_Aires', 'Buenos_Aires'), ('America/Cambridge_Bay', 'Cambridge_Bay'), ('America/Campo_Grande', 'Campo_Grande'), ('America/Cancun', 'Cancun'), ('America/Caracas', 'Caracas'), ('America/Catamarca', 'Catamarca'), ('America/Cayenne', 'Cayenne'), ('America/Cayman', 'Cayman'), ('America/Chicago', 'Chicago'), ('America/Chihuahua', 'Chihuahua'), ('America/Coral_Harbour', 'Coral_Harbour'), ('America/Cordoba', 'Cordoba'), ('America/Costa_Rica', 'Costa_Rica'), ('America/Creston', 'Creston'), ('America/Cuiaba', 'Cuiaba'), ('America/Curacao', 'Curacao'), ('America/Danmarkshavn', 'Danmarkshavn'), ('America/Dawson', 'Dawson'), ('America/Dawson_Creek', 'Dawson_Creek'), ('America/Denver', 'Denver'), ('America/Detroit', 'Detroit'), ('America/Dominica', 'Dominica'), ('America/Edmonton', 'Edmonton'), ('America/Eirunepe', 'Eirunepe'), ('America/El_Salvador', 'El_Salvador'), ('America/Ensenada', 'Ensenada'), ('America/Fort_Nelson', 'Fort_Nelson'), ('America/Fort_Wayne', 'Fort_Wayne'), ('America/Fortaleza', 'Fortaleza'), ('America/Glace_Bay', 'Glace_Bay'), ('America/Godthab', 'Godthab'), ('America/Goose_Bay', 'Goose_Bay'), ('America/Grand_Turk', 'Grand_Turk'), ('America/Grenada', 'Grenada'), ('America/Guadeloupe', 'Guadeloupe'), ('America/Guatemala', 'Guatemala'), ('America/Guayaquil', 'Guayaquil'), ('America/Guyana', 'Guyana'), ('America/Halifax', 'Halifax'), ('America/Havana', 'Havana'), ('America/Hermosillo', 'Hermosillo'), ('America/Indiana/Indianapolis', 'Indiana/Indianapolis'), ('America/Indiana/Knox', 'Indiana/Knox'), ('America/Indiana/Marengo', 'Indiana/Marengo'), ('America/Indiana/Petersburg', 'Indiana/Petersburg'), ('America/Indiana/Tell_City', 'Indiana/Tell_City'), ('America/Indiana/Vevay', 'Indiana/Vevay'), ('America/Indiana/Vincennes', 'Indiana/Vincennes'), ('America/Indiana/Winamac', 'Indiana/Winamac'), ('America/Indianapolis', 'Indianapolis'), ('America/Inuvik', 'Inuvik'), ('America/Iqaluit', 'Iqaluit'), ('America/Jamaica', 'Jamaica'), ('America/Jujuy', 'Jujuy'), ('America/Juneau', 'Juneau'), ('America/Kentucky/Louisville', 'Kentucky/Louisville'), ('America/Kentucky/Monticello', 'Kentucky/Monticello'), ('America/Knox_IN', 'Knox_IN'), ('America/Kralendijk', 'Kralendijk'), ('America/La_Paz', 'La_Paz'), ('America/Lima', 'Lima'), ('America/Los_Angeles', 'Los_Angeles'), ('America/Louisville', 'Louisville'), ('America/Lower_Princes', 'Lower_Princes'), ('America/Maceio', 'Maceio'), ('America/Managua', 'Managua'), ('America/Manaus', 'Manaus'), ('America/Marigot', 'Marigot'), ('America/Martinique', 'Martinique'), ('America/Matamoros', 'Matamoros'), ('America/Mazatlan', 'Mazatlan'), ('America/Mendoza', 'Mendoza'), ('America/Menominee', 'Menominee'), ('America/Merida', 'Merida'), ('America/Metlakatla', 'Metlakatla'), ('America/Mexico_City', 'Mexico_City'), ('America/Miquelon', 'Miquelon'), ('America/Moncton', 'Moncton'), ('America/Monterrey', 'Monterrey'), ('America/Montevideo', 'Montevideo'), ('America/Montreal', 'Montreal'), ('America/Montserrat', 'Montserrat'), ('America/Nassau', 'Nassau'), ('America/New_York', 'New_York'), ('America/Nipigon', 'Nipigon'), ('America/Nome', 'Nome'), ('America/Noronha', 'Noronha'), ('America/North_Dakota/Beulah', 'North_Dakota/Beulah'), ('America/North_Dakota/Center', 'North_Dakota/Center'), ('America/North_Dakota/New_Salem', 'North_Dakota/New_Salem'), ('America/Nuuk', 'Nuuk'), ('America/Ojinaga', 'Ojinaga'), ('America/Panama', 'Panama'), ('America/Pangnirtung', 'Pangnirtung'), ('America/Paramaribo', 'Paramaribo'), ('America/Phoenix', 'Phoenix'), ('America/Port-au-Prince', 'Port-au-Prince'), ('America/Port_of_Spain', 'Port_of_Spain'), ('America/Porto_Acre', 'Porto_Acre'), ('America/Porto_Velho', 'Porto_Velho'), ('America/Puerto_Rico', 'Puerto_Rico'), ('America/Punta_Arenas', 'Punta_Arenas'), ('America/Rainy_River', 'Rainy_River'), ('America/Rankin_Inlet', 'Rankin_Inlet'), ('America/Recife', 'Recife'), ('America/Regina', 'Regina'), ('America/Resolute', 'Resolute'), ('America/Rio_Branco', 'Rio_Branco'), ('America/Rosario', 'Rosario'), ('America/Santa_Isabel', 'Santa_Isabel'), ('America/Santarem', 'Santarem'), ('America/Santiago', 'Santiago'), ('America/Santo_Domingo', 'Santo_Domingo'), ('America/Sao_Paulo', 'Sao_Paulo'), ('America/Scoresbysund', 'Scoresbysund'), ('America/Shiprock', 'Shiprock'), ('America/Sitka', 'Sitka'), ('America/St_Barthelemy', 'St_Barthelemy'), ('America/St_Johns', 'St_Johns'), ('America/St_Kitts', 'St_Kitts'), ('America/St_Lucia', 'St_Lucia'), ('America/St_Thomas', 'St_Thomas'), ('America/St_Vincent', 'St_Vincent'), ('America/Swift_Current', 'Swift_Current'), ('America/Tegucigalpa', 'Tegucigalpa'), ('America/Thule', 'Thule'), ('America/Thunder_Bay', 'Thunder_Bay'), ('America/Tijuana', 'Tijuana'), ('America/Toronto', 'Toronto'), ('America/Tortola', 'Tortola'), ('America/Vancouver', 'Vancouver'), ('America/Virgin', 'Virgin'), ('America/Whitehorse', 'Whitehorse'), ('America/Winnipeg', 'Winnipeg'), ('America/Yakutat', 'Yakutat'), ('America/Yellowknife', 'Yellowknife')]), ('Antarctica', [('Antarctica/Casey', 'Casey'), ('Antarctica/Davis', 'Davis'), ('Antarctica/DumontDUrville', 'DumontDUrville'), ('Antarctica/Macquarie', 'Macquarie'), ('Antarctica/Mawson', 'Mawson'), ('Antarctica/McMurdo', 'McMurdo'), ('Antarctica/Palmer', 'Palmer'), ('Antarctica/Rothera', 'Rothera'), ('Antarctica/South_Pole', 'South_Pole'), ('Antarctica/Syowa', 'Syowa'), ('Antarctica/Troll', 'Troll'), ('Antarctica/Vostok', 'Vostok')]), ('Arctic', [('Arctic/Longyearbyen', 'Longyearbyen')]), ('Asia', [('Asia/Aden', 'Aden'), ('Asia/Almaty', 'Almaty'), ('Asia/Amman', 'Amman'), ('Asia/Anadyr', 'Anadyr'), ('Asia/Aqtau', 'Aqtau'), ('Asia/Aqtobe', 'Aqtobe'), ('Asia/Ashgabat', 'Ashgabat'), ('Asia/Ashkhabad', 'Ashkhabad'), ('Asia/Atyrau', 'Atyrau'), ('Asia/Baghdad', 'Baghdad'), ('Asia/Bahrain', 'Bahrain'), ('Asia/Baku', 'Baku'), ('Asia/Bangkok', 'Bangkok'), ('Asia/Barnaul', 'Barnaul'), ('Asia/Beirut', 'Beirut'), ('Asia/Bishkek', 'Bishkek'), ('Asia/Brunei', 'Brunei'), ('Asia/Calcutta', 'Calcutta'), ('Asia/Chita', 'Chita'), ('Asia/Choibalsan', 'Choibalsan'), ('Asia/Chongqing', 'Chongqing'), ('Asia/Chungking', 'Chungking'), ('Asia/Colombo', 'Colombo'), ('Asia/Dacca', 'Dacca'), ('Asia/Damascus', 'Damascus'), ('Asia/Dhaka', 'Dhaka'), ('Asia/Dili', 'Dili'), ('Asia/Dubai', 'Dubai'), ('Asia/Dushanbe', 'Dushanbe'), ('Asia/Famagusta', 'Famagusta'), ('Asia/Gaza', 'Gaza'), ('Asia/Harbin', 'Harbin'), ('Asia/Hebron', 'Hebron'), ('Asia/Ho_Chi_Minh', 'Ho_Chi_Minh'), ('Asia/Hong_Kong', 'Hong_Kong'), ('Asia/Hovd', 'Hovd'), ('Asia/Irkutsk', 'Irkutsk'), ('Asia/Istanbul', 'Istanbul'), ('Asia/Jakarta', 'Jakarta'), ('Asia/Jayapura', 'Jayapura'), ('Asia/Jerusalem', 'Jerusalem'), ('Asia/Kabul', 'Kabul'), ('Asia/Kamchatka', 'Kamchatka'), ('Asia/Karachi', 'Karachi'), ('Asia/Kashgar', 'Kashgar'), ('Asia/Kathmandu', 'Kathmandu'), ('Asia/Katmandu', 'Katmandu'), ('Asia/Khandyga', 'Khandyga'), ('Asia/Kolkata', 'Kolkata'), ('Asia/Krasnoyarsk', 'Krasnoyarsk'), ('Asia/Kuala_Lumpur', 'Kuala_Lumpur'), ('Asia/Kuching', 'Kuching'), ('Asia/Kuwait', 'Kuwait'), ('Asia/Macao', 'Macao'), ('Asia/Macau', 'Macau'), ('Asia/Magadan', 'Magadan'), ('Asia/Makassar', 'Makassar'), ('Asia/Manila', 'Manila'), ('Asia/Muscat', 'Muscat'), ('Asia/Nicosia', 'Nicosia'), ('Asia/Novokuznetsk', 'Novokuznetsk'), ('Asia/Novosibirsk', 'Novosibirsk'), ('Asia/Omsk', 'Omsk'), ('Asia/Oral', 'Oral'), ('Asia/Phnom_Penh', 'Phnom_Penh'), ('Asia/Pontianak', 'Pontianak'), ('Asia/Pyongyang', 'Pyongyang'), ('Asia/Qatar', 'Qatar'), ('Asia/Qostanay', 'Qostanay'), ('Asia/Qyzylorda', 'Qyzylorda'), ('Asia/Rangoon', 'Rangoon'), ('Asia/Riyadh', 'Riyadh'), ('Asia/Saigon', 'Saigon'), ('Asia/Sakhalin', 'Sakhalin'), ('Asia/Samarkand', 'Samarkand'), ('Asia/Seoul', 'Seoul'), ('Asia/Shanghai', 'Shanghai'), ('Asia/Singapore', 'Singapore'), ('Asia/Srednekolymsk', 'Srednekolymsk'), ('Asia/Taipei', 'Taipei'), ('Asia/Tashkent', 'Tashkent'), ('Asia/Tbilisi', 'Tbilisi'), ('Asia/Tehran', 'Tehran'), ('Asia/Tel_Aviv', 'Tel_Aviv'), ('Asia/Thimbu', 'Thimbu'), ('Asia/Thimphu', 'Thimphu'), ('Asia/Tokyo', 'Tokyo'), ('Asia/Tomsk', 'Tomsk'), ('Asia/Ujung_Pandang', 'Ujung_Pandang'), ('Asia/Ulaanbaatar', 'Ulaanbaatar'), ('Asia/Ulan_Bator', 'Ulan_Bator'), ('Asia/Urumqi', 'Urumqi'), ('Asia/Ust-Nera', 'Ust-Nera'), ('Asia/Vientiane', 'Vientiane'), ('Asia/Vladivostok', 'Vladivostok'), ('Asia/Yakutsk', 'Yakutsk'), ('Asia/Yangon', 'Yangon'), ('Asia/Yekaterinburg', 'Yekaterinburg'), ('Asia/Yerevan', 'Yerevan')]), ('Atlantic', [('Atlantic/Azores', 'Azores'), ('Atlantic/Bermuda', 'Bermuda'), ('Atlantic/Canary', 'Canary'), ('Atlantic/Cape_Verde', 'Cape_Verde'), ('Atlantic/Faeroe', 'Faeroe'), ('Atlantic/Faroe', 'Faroe'), ('Atlantic/Jan_Mayen', 'Jan_Mayen'), ('Atlantic/Madeira', 'Madeira'), ('Atlantic/Reykjavik', 'Reykjavik'), ('Atlantic/South_Georgia', 'South_Georgia'), ('Atlantic/St_Helena', 'St_Helena'), ('Atlantic/Stanley', 'Stanley')]), ('Australia', [('Australia/ACT', 'ACT'), ('Australia/Adelaide', 'Adelaide'), ('Australia/Brisbane', 'Brisbane'), ('Australia/Broken_Hill', 'Broken_Hill'), ('Australia/Canberra', 'Canberra'), ('Australia/Currie', 'Currie'), ('Australia/Darwin', 'Darwin'), ('Australia/Eucla', 'Eucla'), ('Australia/Hobart', 'Hobart'), ('Australia/LHI', 'LHI'), ('Australia/Lindeman', 'Lindeman'), ('Australia/Lord_Howe', 'Lord_Howe'), ('Australia/Melbourne', 'Melbourne'), ('Australia/NSW', 'NSW'), ('Australia/North', 'North'), ('Australia/Perth', 'Perth'), ('Australia/Queensland', 'Queensland'), ('Australia/South', 'South'), ('Australia/Sydney', 'Sydney'), ('Australia/Tasmania', 'Tasmania'), ('Australia/Victoria', 'Victoria'), ('Australia/West', 'West'), ('Australia/Yancowinna', 'Yancowinna')]), ('Brazil', [('Brazil/Acre', 'Acre'), ('Brazil/DeNoronha', 'DeNoronha'), ('Brazil/East', 'East'), ('Brazil/West', 'West')]), ('Canada', [('Canada/Atlantic', 'Atlantic'), ('Canada/Central', 'Central'), ('Canada/Eastern', 'Eastern'), ('Canada/Mountain', 'Mountain'), ('Canada/Newfoundland', 'Newfoundland'), ('Canada/Pacific', 'Pacific'), ('Canada/Saskatchewan', 'Saskatchewan'), ('Canada/Yukon', 'Yukon')]), ('Chile', [('Chile/Continental', 'Continental'), ('Chile/EasterIsland', 'EasterIsland')]), ('Etc', [('Etc/Greenwich', 'Greenwich'), ('Etc/UCT', 'UCT'), ('Etc/UTC', 'UTC'), ('Etc/Universal', 'Universal'), ('Etc/Zulu', 'Zulu')]), ('Europe', [('Europe/Amsterdam', 'Amsterdam'), ('Europe/Andorra', 'Andorra'), ('Europe/Astrakhan', 'Astrakhan'), ('Europe/Athens', 'Athens'), ('Europe/Belfast', 'Belfast'), ('Europe/Belgrade', 'Belgrade'), ('Europe/Berlin', 'Berlin'), ('Europe/Bratislava', 'Bratislava'), ('Europe/Brussels', 'Brussels'), ('Europe/Bucharest', 'Bucharest'), ('Europe/Budapest', 'Budapest'), ('Europe/Busingen', 'Busingen'), ('Europe/Chisinau', 'Chisinau'), ('Europe/Copenhagen', 'Copenhagen'), ('Europe/Dublin', 'Dublin'), ('Europe/Gibraltar', 'Gibraltar'), ('Europe/Guernsey', 'Guernsey'), ('Europe/Helsinki', 'Helsinki'), ('Europe/Isle_of_Man', 'Isle_of_Man'), ('Europe/Istanbul', 'Istanbul'), ('Europe/Jersey', 'Jersey'), ('Europe/Kaliningrad', 'Kaliningrad'), ('Europe/Kiev', 'Kiev'), ('Europe/Kirov', 'Kirov'), ('Europe/Lisbon', 'Lisbon'), ('Europe/Ljubljana', 'Ljubljana'), ('Europe/London', 'London'), ('Europe/Luxembourg', 'Luxembourg'), ('Europe/Madrid', 'Madrid'), ('Europe/Malta', 'Malta'), ('Europe/Mariehamn', 'Mariehamn'), ('Europe/Minsk', 'Minsk'), ('Europe/Monaco', 'Monaco'), ('Europe/Moscow', 'Moscow'), ('Europe/Nicosia', 'Nicosia'), ('Europe/Oslo', 'Oslo'), ('Europe/Paris', 'Paris'), ('Europe/Podgorica', 'Podgorica'), ('Europe/Prague', 'Prague'), ('Europe/Riga', 'Riga'), ('Europe/Rome', 'Rome'), ('Europe/Samara', 'Samara'), ('Europe/San_Marino', 'San_Marino'), ('Europe/Sarajevo', 'Sarajevo'), ('Europe/Saratov', 'Saratov'), ('Europe/Simferopol', 'Simferopol'), ('Europe/Skopje', 'Skopje'), ('Europe/Sofia', 'Sofia'), ('Europe/Stockholm', 'Stockholm'), ('Europe/Tallinn', 'Tallinn'), ('Europe/Tirane', 'Tirane'), ('Europe/Tiraspol', 'Tiraspol'), ('Europe/Ulyanovsk', 'Ulyanovsk'), ('Europe/Uzhgorod', 'Uzhgorod'), ('Europe/Vaduz', 'Vaduz'), ('Europe/Vatican', 'Vatican'), ('Europe/Vienna', 'Vienna'), ('Europe/Vilnius', 'Vilnius'), ('Europe/Volgograd', 'Volgograd'), ('Europe/Warsaw', 'Warsaw'), ('Europe/Zagreb', 'Zagreb'), ('Europe/Zaporozhye', 'Zaporozhye'), ('Europe/Zurich', 'Zurich')]), ('Indian', [('Indian/Antananarivo', 'Antananarivo'), ('Indian/Chagos', 'Chagos'), ('Indian/Christmas', 'Christmas'), ('Indian/Cocos', 'Cocos'), ('Indian/Comoro', 'Comoro'), ('Indian/Kerguelen', 'Kerguelen'), ('Indian/Mahe', 'Mahe'), ('Indian/Maldives', 'Maldives'), ('Indian/Mauritius', 'Mauritius'), ('Indian/Mayotte', 'Mayotte'), ('Indian/Reunion', 'Reunion')]), ('Mexico', [('Mexico/BajaNorte', 'BajaNorte'), ('Mexico/BajaSur', 'BajaSur'), ('Mexico/General', 'General')]), ('Other', [('CET', 'CET'), ('CST6CDT', 'CST6CDT'), ('Cuba', 'Cuba'), ('EET', 'EET'), ('EST', 'EST'), ('EST5EDT', 'EST5EDT'), ('Egypt', 'Egypt'), ('Eire', 'Eire'), ('GB', 'GB'), ('GB-Eire', 'GB-Eire'), ('Greenwich', 'Greenwich'), ('HST', 'HST'), ('Hongkong', 'Hongkong'), ('Iceland', 'Iceland'), ('Iran', 'Iran'), ('Israel', 'Israel'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Kwajalein', 'Kwajalein'), ('Libya', 'Libya'), ('MET', 'MET'), ('MST', 'MST'), ('MST7MDT', 'MST7MDT'), ('NZ', 'NZ'), ('NZ-CHAT', 'NZ-CHAT'), ('Navajo', 'Navajo'), ('PRC', 'PRC'), ('PST8PDT', 'PST8PDT'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('ROC', 'ROC'), ('ROK', 'ROK'), ('Singapore', 'Singapore'), ('Turkey', 'Turkey'), ('UCT', 'UCT'), ('UTC', 'UTC'), ('Universal', 'Universal'), ('W-SU', 'W-SU'), ('WET', 'WET'), ('Zulu', 'Zulu')]), ('Pacific', [('Pacific/Apia', 'Apia'), ('Pacific/Auckland', 'Auckland'), ('Pacific/Bougainville', 'Bougainville'), ('Pacific/Chatham', 'Chatham'), ('Pacific/Chuuk', 'Chuuk'), ('Pacific/Easter', 'Easter'), ('Pacific/Efate', 'Efate'), ('Pacific/Enderbury', 'Enderbury'), ('Pacific/Fakaofo', 'Fakaofo'), ('Pacific/Fiji', 'Fiji'), ('Pacific/Funafuti', 'Funafuti'), ('Pacific/Galapagos', 'Galapagos'), ('Pacific/Gambier', 'Gambier'), ('Pacific/Guadalcanal', 'Guadalcanal'), ('Pacific/Guam', 'Guam'), ('Pacific/Honolulu', 'Honolulu'), ('Pacific/Johnston', 'Johnston'), ('Pacific/Kiritimati', 'Kiritimati'), ('Pacific/Kosrae', 'Kosrae'), ('Pacific/Kwajalein', 'Kwajalein'), ('Pacific/Majuro', 'Majuro'), ('Pacific/Marquesas', 'Marquesas'), ('Pacific/Midway', 'Midway'), ('Pacific/Nauru', 'Nauru'), ('Pacific/Niue', 'Niue'), ('Pacific/Norfolk', 'Norfolk'), ('Pacific/Noumea', 'Noumea'), ('Pacific/Pago_Pago', 'Pago_Pago'), ('Pacific/Palau', 'Palau'), ('Pacific/Pitcairn', 'Pitcairn'), ('Pacific/Pohnpei', 'Pohnpei'), ('Pacific/Ponape', 'Ponape'), ('Pacific/Port_Moresby', 'Port_Moresby'), ('Pacific/Rarotonga', 'Rarotonga'), ('Pacific/Saipan', 'Saipan'), ('Pacific/Samoa', 'Samoa'), ('Pacific/Tahiti', 'Tahiti'), ('Pacific/Tarawa', 'Tarawa'), ('Pacific/Tongatapu', 'Tongatapu'), ('Pacific/Truk', 'Truk'), ('Pacific/Wake', 'Wake'), ('Pacific/Wallis', 'Wallis'), ('Pacific/Yap', 'Yap')]), ('US', [('US/Alaska', 'Alaska'), ('US/Aleutian', 'Aleutian'), ('US/Arizona', 'Arizona'), ('US/Central', 'Central'), ('US/East-Indiana', 'East-Indiana'), ('US/Eastern', 'Eastern'), ('US/Hawaii', 'Hawaii'), ('US/Indiana-Starke', 'Indiana-Starke'), ('US/Michigan', 'Michigan'), ('US/Mountain', 'Mountain'), ('US/Pacific', 'Pacific'), ('US/Samoa', 'Samoa')])], default='Asia/Ho_Chi_Minh', max_length=50, verbose_name='location'),
        ),
    ]
