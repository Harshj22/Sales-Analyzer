import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.file_path = r"C:\Users\Asus\Downloads\sales_data.csv"
        self.data = None

    def load_dataset(self):
        self.data = pd.read_csv(self.file_path)
        print("Dataset loaded successfully!")

    def explore_data(self):
        print("\nFirst 5 rows:\n", self.data.head())
        print("\nLast 5 rows:\n", self.data.tail())
        print("\nColumn Names:\n", self.data.columns)
        print("\nData Info:")
        print(self.data.info())

    def dataframe_operations(self):
        print("\nTotal Sales:", self.data["Sales"].sum())
        print("Average Sales:", self.data["Sales"].mean())
        print("Total Profit:", self.data["Profit"].sum())

    def handle_missing_data(self):
        print("\nMissing values:\n", self.data.isnull().sum())
        self.data.fillna(0, inplace=True)
        print("Missing values handled.")

    def descriptive_statistics(self):
        print("\nDescriptive Statistics:\n")
        print(self.data.describe())

    def data_visualization(self):
        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")

        choice = input("Enter your choice: ")

        plt.figure(figsize=(10, 6))
        sns.set_style("darkgrid")

        if choice == "1":
            sns.barplot(x="Region", y="Sales", data=self.data, hue="Payment_Mode", palette="viridis")
            plt.legend(loc="upper right")
            plt.title("Sales by Region")
            plt.savefig("bar_plot.png", dpi=300)
            plt.show()

        elif choice == "2":
            sns.lineplot(data=self.data, x="Date", y="Sales", hue="Region", palette="viridis", linewidth=2,
                         alpha=0.7, marker="o", markersize=5)

            plt.title("Sales Trend Over Time")
            plt.xlabel("Date")
            plt.ylabel("Sales")
            plt.savefig("line_plot.png", dpi=300)
            plt.show()

        elif choice == "3":
            sns.scatterplot(x="Sales", y="Profit", data=self.data, hue="Region", palette="coolwarm")
            plt.legend(loc="upper right")
            plt.title("Sales vs Profit")
            plt.savefig("scatter_plot.png", dpi=300)
            plt.show()

        elif choice == "4":
            plt.pie(self.data["Sales"][:6], labels=self.data["Product"][:6], autopct="%1.1f%%", startangle=90, 
                    colors=sns.color_palette("viridis"), shadow=True, explode=[0.1]*6)
            plt.title("Sales Distribution (Sample Products)")
            plt.savefig("pie_chart.png", dpi=300)
            plt.show()

        elif choice == "5":
            sns.histplot(self.data["Sales"], bins=10, color="#157F85", edgecolor="black", zorder=3)
            plt.title("Sales Distribution")
            plt.xlabel("Sales")
            plt.ylabel("Frequency")
            plt.savefig("histogram.png", dpi=300)
            plt.show()

        elif choice == "6":
            plt.stackplot(range(5), self.data["Sales"][:5], labels=self.data["Product"][:5], color="#29366F", 
                          alpha=0.7, edgecolor="black", linewidth=1)
            plt.legend(loc="upper right")
            plt.xlabel("Index")
            plt.ylabel("Sales")
            plt.title("Stack Plot of Sales")
            plt.savefig("stack_plot.png", dpi=300)
            plt.tight_layout()
            plt.show()


def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.load_dataset()
        elif choice == "2":
            analyzer.explore_data()
        elif choice == "3":
            analyzer.dataframe_operations()
        elif choice == "4":
            analyzer.handle_missing_data()
        elif choice == "5":
            analyzer.descriptive_statistics()
        elif choice == "6":
            analyzer.data_visualization()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
