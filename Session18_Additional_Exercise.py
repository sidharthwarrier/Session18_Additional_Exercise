{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem Statement\n",
    "Given the following data set, use the sklearn package to find the co-efficients of the\n",
    "line that describes the following relationships:\n",
    "1) x1 and y\n",
    "2) x2 and y\n",
    "3) x3 and y\n",
    "Also, plot the line and the data using matplotlib and report the co-efficient of\n",
    "determination for the lines using the metrics library."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "## importing required libraries\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import scipy.stats as stats\n",
    "import matplotlib.pyplot as plt\n",
    "import sklearn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "df =pd.read_csv(\"Data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
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
       "      <th>SI No.</th>\n",
       "      <th>TV</th>\n",
       "      <th>Radio</th>\n",
       "      <th>Newspaper</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>230.1</td>\n",
       "      <td>37.8</td>\n",
       "      <td>69.2</td>\n",
       "      <td>22.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>44.5</td>\n",
       "      <td>39.3</td>\n",
       "      <td>45.1</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>17.2</td>\n",
       "      <td>45.9</td>\n",
       "      <td>69.3</td>\n",
       "      <td>9.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>151.5</td>\n",
       "      <td>41.3</td>\n",
       "      <td>58.5</td>\n",
       "      <td>18.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>180.8</td>\n",
       "      <td>10.8</td>\n",
       "      <td>58.4</td>\n",
       "      <td>12.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   SI No.      TV  Radio  Newspaper  Sales\n",
       "0        1  230.1   37.8       69.2   22.1\n",
       "1        2   44.5   39.3       45.1   10.4\n",
       "2        3   17.2   45.9       69.3    9.3\n",
       "3        4  151.5   41.3       58.5   18.5\n",
       "4        5  180.8   10.8       58.4   12.9"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     69.2\n",
       "1     45.1\n",
       "2     69.3\n",
       "3     58.5\n",
       "4     58.4\n",
       "5     75.0\n",
       "6     23.5\n",
       "7     11.6\n",
       "8      1.0\n",
       "9     21.2\n",
       "10    24.2\n",
       "11     4.0\n",
       "12    65.9\n",
       "13     7.2\n",
       "14    46.0\n",
       "Name: Newspaper, dtype: float64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Newspaper']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.040610598249053\n",
      "[ 0.05461004  0.17104816 -0.02717817]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "lm = LinearRegression()\n",
    "# Creating Independent(X) and Dependent(Target-Y) data frames\n",
    "X = df[['TV', 'Radio','Newspaper']]\n",
    "Y = df['Sales']\n",
    "lm.fit(X, Y)\n",
    "# print intercept and coefficients\n",
    "print(lm.intercept_)\n",
    "print(lm.coef_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x360 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting the X1,X2 and X3 against Sales\n",
    "plt.figure(figsize=(20, 5))\n",
    "\n",
    "# iterating for each column \n",
    "for i, col in enumerate(['TV', 'Radio', 'Newspaper']):\n",
    "    plt.subplot(1, 3, i+1)\n",
    "    x = df[col]\n",
    "    y = df['Sales']\n",
    "    plt.plot(x, y, 'o')\n",
    "    # Create regression line\n",
    "    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))\n",
    "    plt.title(col)\n",
    "    plt.xlabel(col)\n",
    "    plt.ylabel('Sales')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
