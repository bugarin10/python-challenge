#This code make a summary analysis, the first one analyses the records of a company
#the second one analyzes votes returning the winner

import os
import pandas as pd
import csv
import numpy as np

#------------ FINANCIAL ANALYSIS --------------------

csvpath = os.path.join('Resources', 'budget_data.csv')

data=pd.read_csv(csvpath,sep=',')

total_months=len(data.Date.unique())
net_total=sum(data['Profit/Losses'])
diffs=data['Profit/Losses'].diff()
avg_ch=diffs.mean()
idx_max=np.where(np.array(diffs)==diffs.max())[0][0]
max_month=data.Date[idx_max]
max_inc=diffs[idx_max]

idx_min=np.where(np.array(diffs)==diffs.min())[0][0]
min_month=data.Date[idx_min]
min_inc=diffs[idx_min]


#Print the analysis

print('Financial Analysis')
print('--------------------------')
print(f'Total months: {net_total}')
print(f'Total: {total_months}')
print(f'Average Change: ${avg_ch}')
print(f'Greatest Increase in Profits: {max_month} (${max_inc})')
print(f'Greatest Decrease in Profits: {min_month} (${min_inc})')

#Export the analysis

txtpath = os.path.join('Analysis', 'Financial analysis.txt')
f = open(txtpath,'w')
f.write('Financial Analysis\n')
f.write('--------------------------\n')
f.write(f'Total months: {net_total}\n')
f.write(f'Total: {total_months}\n')
f.write(f'Average Change: ${avg_ch}\n')
f.write(f'Greatest Increase in Profits: {max_month} (${max_inc})\n')
f.write(f'Greatest Decrease in Profits: {min_month} (${min_inc})\n')
f.close()

#------------ VOTES ANALYSIS --------------------

csvpath = os.path.join('Resources', 'election_data.csv')
data=pd.read_csv(csvpath,sep=',')


tot_votes=len(data['Voter ID'].unique())
data_agg=data[['Candidate','Voter ID']].groupby('Candidate',as_index=False).count()
data_agg.rename(columns={'Voter ID':'total'},inplace=True)
tot=data_agg.total.sum()
vot_max=np.where(np.array(data_agg['total'])==data_agg['total'].max())[0][0]

#Print results

print('\nElection Results\n')
print('--------------------------\n')

for i in list(range(data_agg.shape[0])):
    print(f'{data_agg.iloc[i,0]}: {data_agg.iloc[i,1]*100/tot:.3f}% ({data_agg.iloc[i,1]})\n')
    
print('--------------------------\n')
print(f'Winner is: {data_agg.iloc[vot_max,0]}\n')

#Export results

txtpath = os.path.join('Analysis', 'Polls analysis.txt')
f = open(txtpath,'w')
f.write('Election Results\n')
f.write('--------------------------\n')

for i in list(range(data_agg.shape[0])):
    f.write(f'{data_agg.iloc[i,0]}: {data_agg.iloc[i,1]*100/tot:.3f}% ({data_agg.iloc[i,1]})\n')
    
f.write('--------------------------\n')

f.write(f'Winner is: {data_agg.iloc[vot_max,0]}')

f.close()