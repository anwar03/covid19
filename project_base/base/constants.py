import pytz
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Token
TOKEN_KEY = 'TOKEN_KEY'

# common timezone from pytz
TIMEZONE_CHOICES = [(t, t) for t in pytz.common_timezones]

# languages
ENGLISH, SWEDISH = 'en', 'sv'
PREFERRED_LANGUAGE = ((ENGLISH, 'English'), (SWEDISH, 'Swedish'))

FIXED_COST, DAILY_COST, HOURLY_COST, WEEKLY_COST = 'fixed_cost', 'daily_cost', 'hourly_cost', 'weekly_cost'
COST_TYPE = ((FIXED_COST, _('Fixed')), (DAILY_COST, _('Daily')), (HOURLY_COST, _('Hourly')), (WEEKLY_COST, _('Weekly')))

DAILY, HOURLY, WEEKLY, MONTHLY = 'daily', 'hourly', 'weekly', 'monthly'
TIME_ESTIMATION_TYPE = ((DAILY, _('daily')), (HOURLY, _('Hourly')), (WEEKLY, _('Weekly')), (MONTHLY, _('Monthly')))

# leave types
SICK_LEAVE = 1
PAID_LEAVE = 2
UNPAID_LEAVE = 3
ANNUAL_LEAVE = 4
FAMILY_LEAVE = 5
LEAVE_TYPES = ((SICK_LEAVE, _('Sick Leave')), (PAID_LEAVE, _('Paid Leave')),
               (UNPAID_LEAVE, _('Unpaid Leave')), (ANNUAL_LEAVE, _('Annual Leave')),
               (FAMILY_LEAVE, _('Family Leave')))

# Year
CURRENT_YEAR = timezone.datetime.now().year

START_YEAR = CURRENT_YEAR - 5
END_YEAR = CURRENT_YEAR + 10

YEARS = [(year, _(str(year))) for year in range(START_YEAR, END_YEAR)]
