class ATM:
    def __init__(self):
        # Notes available in ATM (descending order — greedy requirement)
        self.notes = [2000, 500, 200, 100]

        # Cash stock in ATM (realistic simulation)
        self.stock = {
            2000: 50,
            500:  100,
            200:  150,
            100:  200
        }

    def dispense(self, amount):
        # Validation
        if amount <= 0:
            return "❌ Invalid amount"
        if amount % 100 != 0:
            return "❌ Amount must be multiple of 100"
        if amount > self.total_cash():
            return "❌ Insufficient cash in ATM"

        result = {}
        remaining = amount

        # GREEDY:
        for note in self.notes:
            if remaining >= note:
                count = remaining // note
                # Stock check
                count = min(count, self.stock[note])
                if count > 0:
                    result[note] = count
                    remaining -= count * note

    
        if remaining != 0:
            return f"❌ Cannot dispense ₹{amount}. Try different amount."

        # Stock update
        for note, count in result.items():
            self.stock[note] -= count

        return result

    def total_cash(self):
        return sum(note * qty for note, qty in self.stock.items())

    def show_stock(self):
        print("\n📦 Current ATM Stock:")
        for note, qty in self.stock.items():
            print(f"   ₹{note} × {qty} = ₹{note * qty}")
        print(f"   Total: ₹{self.total_cash()}")


# ---------- MAIN ----------
if __name__ == "__main__":
    atm = ATM()

    print("=== ATM Cash Dispenser (Greedy Strategy) ===")
    print("Available Notes: ₹2000, ₹500, ₹200, ₹100\n")

    atm.show_stock()

    # Test cases
    test_amounts = [3800, 2500, 100, 6700, 999, 50000]

    for amt in test_amounts:
        print(f"\n--- Withdraw ₹{amt} ---")
        result = atm.dispense(amt)

        if isinstance(result, dict):
            total_notes = sum(result.values())
            print(f"✅ Dispensed {total_notes} notes:")
            for note in sorted(result.keys(), reverse=True):
                print(f"   ₹{note} × {result[note]} = ₹{note * result[note]}")
        else:
            print(result)

    atm.show_stock()