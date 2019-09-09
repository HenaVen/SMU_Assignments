{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import dependencies\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\henat\\Desktop\\SMUGitLab\\SMU_Assignments\\Unit_03_Python\\budget_data.csv\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Profit/Losses\n",
       "0  Jan-2010         867884\n",
       "1  Feb-2010         984655\n",
       "2  Mar-2010         322013\n",
       "3  Apr-2010         -69417\n",
       "4  May-2010         310503"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#load and read the budget.csv file\n",
    "budget_csv='C:\\\\Users\\\\henat\\\\Desktop\\\\SMUGitLab\\\\SMU_Assignments\\\\Unit_03_Python\\\\budget_data.csv'\n",
    "print(budget_csv)\n",
    "# budget2_csv='C:\\\\Users\\\\henat\\\\Desktop\\\\SMUGitLab\\\\SMU-DAL-DATA-PT-08-2019-U-C\\\\02-Homework\\\\03-Python\\\\Instructions\\\\PyBank\\\\Resources\\\\budget_data.csv'\n",
    "#Read csv to dataframe\n",
    "budget_df=pd.read_csv(budget_csv,encoding=\"ISO-8859-1\")\n",
    "budget_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date             86\n",
      "Profit/Losses    86\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#1.The total number of months included in the dataset\n",
    "#len of dataframe\n",
    "#MonthCount=len(budget_df.[\"Date\"].unique())\n",
    "#MonthCount=budget_df.[\"Date\"].value_counts()\n",
    "budget_df.head()\n",
    "print(budget_df.count())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "86\n"
     ]
    }
   ],
   "source": [
    "#The total number of months included in the dataset\n",
    "month_count= budget_df[\"Date\"].value_counts().sum()\n",
    "print(month_count)\n",
    "#lengthmonth=month_count[0].sum()\n",
    "#lengthmonth"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "38382578"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#The net total amount of \"Profit/Losses\" over the entire period\n",
    "Total_PnL= budget_df[\"Profit/Losses\"].sum()\n",
    "Total_PnL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "446309.0465116279"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#The average of the changes in \"Profit/Losses\" over the entire period\n",
    "Avg_PnL= budget_df[\"Profit/Losses\"].mean()\n",
    "Avg_PnL\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1170593"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#The greatest increase in profits (date and amount) over the entire period\n",
    "Greatest_PnL= budget_df[\"Profit/Losses\"].max()\n",
    "Greatest_PnL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feb-2012 1170593\n"
     ]
    }
   ],
   "source": [
    "print (budget_df.loc[budget_df[\"Profit/Losses\"].idxmax(),\"Date\"],Greatest_PnL)\n",
    "#Greatest_PnLloc\n",
    "#print(budget_df[25])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sep-2013 -1196225\n"
     ]
    }
   ],
   "source": [
    "#The greatest decrease in losses (date and amount) over the entire period\n",
    "Greatest_Loss= budget_df[\"Profit/Losses\"].min()\n",
    "print (budget_df.loc[budget_df[\"Profit/Losses\"].idxmin(),\"Date\"],Greatest_Loss)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        Date  Profit/Losses\n",
      "25  Feb-2012        1170593\n"
     ]
    }
   ],
   "source": [
    "print(budget_df.loc[[25]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date             Feb-2012\n",
      "Profit/Losses     1170593\n",
      "Name: 25, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(budget_df.loc[budget_df[\"Profit/Losses\"].idxmax()])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#df = pd.DataFrame()\n",
    "\n",
    "#df[\"MinYear\"] = [sum_df[0],1]\n",
    "#df[\"MaxYear\"] = [sum_df[1],1]\n",
    "#df[\"Total\"] = [sum_df[2],1]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
