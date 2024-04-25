#!/usr/bin/env python3

import argparse
from typing import List
import pyperclip


def _parse_email(value):
    return value.replace("<", "").replace(">", "")


def _parse_username(value):
    return value.split('@')[0]


def _extract_metadata(value):
    name = None
    email = None
    username = None

    if len(value) > 1:
        name = value[0]
        email = value[-1]
    elif '@' in value[0]:
        email = value[0]
    else:
        name = value[0]

    email = _parse_email(email) if email is not None else None

    if email is not None:
        username = _parse_username(email)

    return {
        'name': name,
        'email': email,
        'username': username,
    }


def _parse_participants(raw_participants: str) -> List[dict]:
    participants = [value.strip() for value in raw_participants.split(',')]
    participants = [value.split(' <') for value in participants]
    print(participants)
    participants = [_extract_metadata(value) for value in participants]
    print(participants)

    return participants


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--calendar-deltagere', nargs='+')

    args = parser.parse_args()

    participants = ([_parse_participants(raw_participants) for raw_participants in args.calendar_deltagere])
    participants = [item for sublist in participants for item in sublist]

    participant_usernames = {participant['username'] for participant in participants}

    print('Deltagere')
    for participant in participants:
        print(f'  - {participant["name"]} {participant["email"]}')

    print('')
    print(f'Til utlegget: {", ".join(participant_usernames)}')
    pyperclip.copy(", ".join(participant_usernames))
    print('Kopiert til clipboard!')


if __name__ == '__main__':
    main()
