import contacts
print('Address Book Notes')
print('=' * 40)
people = contacts.get_all_people()
for p in people:
  note = p.note
  if note:
    print(p.full_name)
    print('-' * 40)
    print(note)
    print('=' * 40)