import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


def remove_sac_events(df):
    #remove sac events from data since they are not considered at bats'
    sac_events = ['sac_bunt', 'sac_fly', 'sac_fly_double_play', 'sac_bunt_double_play']
    df_ = df[-df['event_type'].isin(sac_events)]
    return df_


def get_kde_dist_plots(before_imputing, after_imputing, label='hit_spin_rate'):
    # create kde distribution plots of a column before and after imputation
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(before_imputing.dropna(), bins=20, kde=True, color='blue', label='Original')
    plt.title(f'Distribution of {label} (Original)')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.legend()

    plt.subplot(1, 2, 2)
    sns.histplot(after_imputing, bins=20, kde=True, color='orange', label='Imputed')
    plt.title(f'Distribution of {label} (After Imputation)')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.legend()

    # Summary Statistics (Before and After Imputation)
    print("Summary Statistics - Original:")
    print(before_imputing.describe())
    print("\nSummary Statistics - Imputed:")
    print(after_imputing.describe())

    # QQ - quantile plots
    plt.figure(figsize=(6, 4))
    stats.probplot(before_imputing.dropna(), dist='norm', plot=plt)
    plt.title('Q-Q Plot - Original')
    plt.show()

    plt.figure(figsize=(6, 4))
    stats.probplot(after_imputing, dist='norm', plot=plt)
    plt.title('Q-Q Plot - Imputed')
    plt.show()