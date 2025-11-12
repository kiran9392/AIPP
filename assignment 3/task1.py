# 🔌 TGNPDCL Custom Electricity Bill Generator

def calculate_bill(previous_units, current_units, customer_type, rate_per_unit, fixed_charge, customer_charge, duty_percent):
    """
    Calculates the electricity bill based on user-provided values.
    """
    # Calculate units consumed
    units = current_units - previous_units
    if units < 0:
        raise ValueError("Current reading cannot be less than previous reading!")

    # Calculate each component
    energy_charge = units * rate_per_unit
    electricity_duty = energy_charge * (duty_percent / 100)
    total_bill = energy_charge + fixed_charge + customer_charge + electricity_duty

    # Return results
    return {
        "Customer Type": customer_type.capitalize(),
        "Units Consumed": units,
        "EC (Energy Charges)": energy_charge,
        "FC (Fixed Charges)": fixed_charge,
        "CC (Customer Charges)": customer_charge,
        "ED (Electricity Duty)": electricity_duty,
        "Total Bill": total_bill
    }


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    print("⚡ TGNPDCL BILL CALCULATOR ⚡\n")

    try:
        # Basic readings
        pu = float(input("Enter Previous Unit Reading (PU): "))
        cu = float(input("Enter Current Unit Reading (CU): "))
        ctype = input("Enter Type of Customer (Domestic/Commercial): ")

        # User-defined rates
        rate = float(input("Enter Rate per Unit (₹): "))
        fc = float(input("Enter Fixed Charge (₹): "))
        cc = float(input("Enter Customer Charge (₹): "))
        ed = float(input("Enter Electricity Duty (%): "))

        # Calculate
        bill = calculate_bill(pu, cu, ctype, rate, fc, cc, ed)

        # Print Bill
        print("\n--- BILL SUMMARY ---")
        for k, v in bill.items():
            if isinstance(v, (int, float)):
                print(f"{k}: ₹{v:.2f}")
            else:
                print(f"{k}: {v}")

    except ValueError as e:
        print("Error:", e)
