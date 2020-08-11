import pandas as pd

def get_user_agents():
    df = pd.read_csv('/home/mahmoud/Downloads/whatismybrowser-user-agent-database.csv')
    user_agents = set(df[df['operating_system_name_code'].isin(list(df['operating_system_name_code'].dropna().unique()))]['user_agent'])
    return user_agents

