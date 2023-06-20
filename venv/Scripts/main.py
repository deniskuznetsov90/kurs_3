from utils import load_data, executed_operations, last_operations, account_mask, card_mask, date

filepath = 'operations.json'
load_data(filepath)
operations = load_data(filepath)
executed_operations(operations)
list_last_operation = last_operations(executed_operations(operations))

list_total = []
mask_from = ()

for operation in list_last_operation:
    operation_date = date(operation['date'])
    if operation.get('from') is None:
        pass

    elif operation.get('from').startswith("Счет"):
        mask_from = account_mask(operation.get('from'))

    else:
        mask_from = card_mask(operation.get('from'))

    if operation.get('to') is None:
        pass
    elif operation.get('to').startswith("Счет"):
        mask_to = account_mask(operation.get('to'))

    else:
        mask_to = card_mask(operation.get('to'))

    print(f'{operation_date} {operation["description"]}\n{mask_from} -> {mask_to}\n'
          f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
