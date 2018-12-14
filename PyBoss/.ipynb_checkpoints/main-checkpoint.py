{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "first_name = \"\"\n",
    "last_name = \"\"\n",
    "form_name = []\n",
    "form_birth = \"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1991', '02', '24']\n"
     ]
    }
   ],
   "source": [
    "with open('employee_data.csv', 'r') as f:\n",
    "    reader = csv.reader(f,)\n",
    "    next(reader)\n",
    "    for row in reader:\n",
    "        first_name = row[1].split(\" \")[0]\n",
    "        last_name = row[1].split(\" \")[1]\n",
    "        form_name = [last_name, first_name]\n",
    "        birth_split = row[2].split(\"-\")\n",
    "        break\n",
    "print(form_birth)"
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
