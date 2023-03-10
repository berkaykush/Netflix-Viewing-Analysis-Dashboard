from .viewing_activity_data import load_viewing_activity_data
from .top_10_most_viewed_titles_data import create_top_10_most_viewed_titles_data
from .daily_hours_watched_data import create_daily_hours_watched_data
from .monthly_hours_watched_data import create_monthly_hours_watched_data

DATA_PATH = "csv_data/ViewingActivity.csv"


class NetflixAnalysisData:
    VIEWING_ACTIVITY = load_viewing_activity_data(DATA_PATH)
    TOP_10_MOST_VIEWED_TITLES = create_top_10_most_viewed_titles_data(VIEWING_ACTIVITY)
    DAILY_HOURS_WATCHED = create_daily_hours_watched_data(VIEWING_ACTIVITY)
    MONTHLY_HOURS_WATCHED = create_monthly_hours_watched_data(VIEWING_ACTIVITY)
