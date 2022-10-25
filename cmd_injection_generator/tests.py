import pytest
from helpers import special_character_to_url_encode, \
    base_64_encode, \
    brace_expansion, \
    character_insertion, \
    reverse_commands


@pytest.fixture()
def user_command():
    return 'find /usr/share/ | grep root | grep mysql | tail -n 1'


def test_special_character_to_url_encode(user_command):
    user_input = special_character_to_url_encode(user_command)
    expected_result = ['find /usr/share/ | grep root | grep mysql | tail -n 1',
                       'find%20/usr/share/%20|%20grep%20root%20|%20grep%20mysql%20|%20tail%20-n%201',
                       'find %2fusr%2fshare%2f | grep root | grep mysql | tail -n 1',
                       'find%20%2fusr%2fshare%2f%20|%20grep%20root%20|%20grep%20mysql%20|%20tail%20-n%201',
                       'find /usr/share/ %7c grep root %7c grep mysql %7c tail -n 1',
                       'find%20/usr/share/%20%7c%20grep%20root%20%7c%20grep%20mysql%20%7c%20tail%20-n%201',
                       'find %2fusr%2fshare%2f %7c grep root %7c grep mysql %7c tail -n 1',
                       'find%20%2fusr%2fshare%2f%20%7c%20grep%20root%20%7c%20grep%20mysql%20%7c%20tail%20-n%201']
    assert user_input == expected_result


def test_base_64_encode(user_command):
    user_input = base_64_encode(user_command)
    expected_result = 'bash<<<$(base64%09-d<<<ZmluZCAvdXNyL3NoYXJlLyB8IGdyZXAgcm9vdCB8IGdyZXAgbXlzcWwgfCB0YWlsIC1uIDE=)'
    assert user_input == expected_result


def test_brace_expansion(user_command):
    user_input = brace_expansion(user_command)
    expected_result = '{find,/usr/share/,|,grep,root,|,grep,mysql,|,tail,-n,1}'
    assert user_input == expected_result


def test_character_insertion(user_command):
    user_input = character_insertion(user_command)
    expected_result = 'f"i"n"d" "/"u"s"r"/"s"h"a"r"e"/" "|" "g"r"e"p" "r"o"o"t" "|" "g"r"e"p" "m"y"s"q"l" "|" "t"a"i"l" "-"n" "1""'
    assert user_input == expected_result


def test_reverse_command(user_command):
    user_input = reverse_commands(user_command)
    expected_result = "$(rev<<<'1 n- liat | lqsym perg | toor perg | /erahs/rsu/ dnif')"
    assert user_input == expected_result
