import matplotlib
matplotlib.use('Agg') # required for Flask to serve matplotlib images
import matplotlib.pyplot as plt # noqa 

def create_plot(df, user_selected_1):

    ########################################################################
    # Create filter DF based on user value
    if user_selected_1 and user_selected_1 != 'Select All':
        output_df = df[df['condition'] == user_selected_1]
    else:
        output_df = df

    ########################################################################
    # Create matplotlib chart
    fig, ax = plt.subplots(figsize=(10, 7))

    main_color = '#1f75fe'  
    highlight_color = '#ee204d' 

    ax.bar(df['condition'], df['condition_count'], color=main_color, alpha=0.7, label='All Conditions')  # noqa 
    ax.bar(output_df['condition'], output_df['condition_count'], color=highlight_color, alpha=0.9, label='Selected Condition')  # noqa
    ax.axhline(y=df['condition_count'].mean(), color='red', linestyle='--', label=f'Mean: ${(df["condition_count"].mean()).round(2):,}')  # noqa

    # Fonts and rotations for labels
    ax.set_xticklabels(df['condition'], rotation=70, ha='right', fontsize=10)
    ax.set_title('Condition Counts', fontsize=16, fontweight='bold', pad=20) 
    ax.set_xlabel('Condition Name', fontsize=14, labelpad=15)
    ax.set_ylabel('Condition Count', fontsize=14, labelpad=15)

    fig.tight_layout()

    return fig