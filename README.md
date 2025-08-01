# 💸 Smart Budgeting System

A simple and intuitive expense tracking application built with Streamlit that helps you monitor your spending habits and visualize your financial data.

## ✨ Features

- **Easy Expense Entry**: Quick form to add expenses with date, item name, and amount
- **Data Persistence**: All expenses are automatically saved to a CSV file
- **Date Range Filtering**: Filter expenses by custom date ranges
- **Interactive Visualizations**:
  - Daily spending trends with cumulative totals
  - Monthly spending summaries
  - Top 10 most expensive items
- **Data Export**: Download your expense data as CSV
- **Clear History**: Reset all expense data when needed
- **Responsive Design**: Clean, mobile-friendly interface

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/smart-budgeting-system.git
cd smart-budgeting-system
```

2. Install the required dependencies:
```bash
pip install streamlit pandas
```

### Running the Application

1. Navigate to the project directory
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your web browser and go to `http://localhost:8501`

## 📱 Usage

### Adding Expenses
1. Select the date of your expense
2. Enter the item name/description
3. Input the amount in Malaysian Ringgit (RM)
4. Click "Add" to save the expense

### Viewing Data
- **Expense History**: View all your expenses in a sortable table
- **Date Filtering**: Use the date range selector to filter expenses
- **Total Spending**: See your total expenses for the selected period

### Visualizations
- **Spending Over Time**: Line chart showing daily expenses and cumulative spending
- **Monthly Totals**: Bar chart displaying spending by month
- **Top Items**: Bar chart of your most expensive purchases

### Data Management
- **Export**: Download your expense data as a CSV file
- **Clear History**: Remove all expense records (use with caution!)

## 📁 File Structure

```
smart-budgeting-system/
│
├── app.py              # Main Streamlit application
├── expenses.csv        # Auto-generated expense data file
├── README.md          # This file
└── requirements.txt   # Python dependencies
```

## 💾 Data Storage

The application automatically creates and maintains an `expenses.csv` file in the same directory. This file contains all your expense data with the following columns:
- **Date**: Date of the expense
- **Item**: Description of the expense
- **Amount (RM)**: Cost in Malaysian Ringgit

## 🛠️ Technical Details

- **Framework**: Streamlit
- **Data Processing**: Pandas
- **Data Storage**: CSV file
- **Date Handling**: Python datetime
- **Visualization**: Streamlit's built-in charting

## 📊 Sample Data Format

| Date       | Item           | Amount (RM) |
|------------|----------------|-------------|
| 2024-01-15 | Groceries      | 45.50       |
| 2024-01-16 | Coffee         | 8.90        |
| 2024-01-17 | Lunch          | 12.00       |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 Future Enhancements

- [ ] Add expense categories
- [ ] Budget limits and alerts
- [ ] Income tracking
- [ ] Multiple currency support
- [ ] Data backup to cloud storage
- [ ] Expense analytics and insights
- [ ] Mobile app version

## ⚠️ Important Notes

- Data is stored locally in a CSV file
- Make regular backups of your `expenses.csv` file
- The application is designed for Malaysian Ringgit (RM) but can be adapted for other currencies

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you encounter any issues or have questions, please create an issue in the GitHub repository.

---

Made with ❤️ using Streamlit
