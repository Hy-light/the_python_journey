def long_word(s1,s2):
    return ''.join(sorted(set(s1 + s2)))

print(long_word('abkkklsknnnnklt', 'hhjtlshntabbtos'))
print(long_word('thejnlsuiojlls', 'ppatnnoemcjtstsa'))

