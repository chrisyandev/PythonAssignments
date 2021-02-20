class BudgetManager:

    def __init__(self, budget, user):
        self._budget = budget
        self._user = user
        self._do_notify = True
        self._do_warn = True
        self._show_transactions = False
        self._budget_locked_count = 0

    def trigger(self):
        if self._do_warn:
            self.warn()
        if self._do_notify:
            self.notify()
        self.lock_budget_if_exceed()
        input("Press ENTER to continue")
        if self._show_transactions:
            self._budget.print_all_transactions()
            input("Press ENTER to continue")
            self._show_transactions = False

    def notify(self):
        amount_spent = self._budget.amount_spent
        total_amount = self._budget.total_amount
        category_name = self._budget.category.name
        if amount_spent > total_amount:
            print("--------------------------------------------------")
            print(f"Note: You've exceeded your entire budget "
                  f"for {category_name}")
            print("--------------------------------------------------")
            self._show_transactions = True
            if self._user.__class__.notify_once:
                self._do_notify = False

    def warn(self):
        amount_spent = self._budget.amount_spent
        total_amount = self._budget.total_amount
        category_name = self._budget.category.name
        warning_threshold = self._user.__class__.warning_threshold
        if amount_spent > total_amount * warning_threshold:
            print("--------------------------------------------------")
            print(f"Warning: You've exceeded {warning_threshold * 100}"
                  f"% of your budget for {category_name}")
            print("--------------------------------------------------")
            self._show_transactions = True
            if self._user.__class__.warn_once:
                self._do_warn = False

    def lock_budget_if_exceed(self):
        budget_lock_threshold = self._user.__class__.budget_lock_threshold
        if budget_lock_threshold is not None:
            amount_spent = self._budget.amount_spent
            total_amount = self._budget.total_amount
            category_name = self._budget.category.name
            if amount_spent > total_amount * budget_lock_threshold:
                self._budget.set_lock(True)
                self._budget_locked_count += 1
                print("-------------------------------------------")
                print(f"Your budget for {category_name} was locked")
                print("-------------------------------------------")
                self.lock_account_if_exceed()

    def lock_account_if_exceed(self):
        account_lock_threshold = self._user.__class__.account_lock_threshold
        if account_lock_threshold is not None:
            if self._budget_locked_count >= account_lock_threshold:
                for budget in self._user.get_all_budgets():
                    budget.set_lock(True)
                    print("-----------------------")
                    print("Your account was locked")
                    print("-----------------------")
