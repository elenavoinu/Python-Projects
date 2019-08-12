# author Elena Voinu

class InventoryTag:
    def __init__(self):
        self.item_id = 0
        self.quantity_remaining = 0

red_sweater = InventoryTag()
red_sweater.item_id = 314
red_sweater.quantity_remaining = 500

''' Your solution goes here '''
print("ID:", red_sweater.item_id)
print("Qty:",red_sweater.quantity_remaining)