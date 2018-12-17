def edit_distance(a, b, show_opt=False):
    """Compute minimal edit distance of two sequences a and b.

    Compute minimal edit distance based on dynamic programming. 
    Minimal edit distance is the minimal number of operations that change a sequence to another.
    There are three kinds of operations: insert, delete, replace.
    For example, the minimal edit distance of 'vintner' and 'writers' is 5.
    Let m[i][j] denote the minimal edit distance of a[1..i] and b[1..j], 
    the recursive relationship are:
    m[i][j] = min{m[i-1][j]+1, m[i][j-1]+1, m[i-1][j-1]+t[i][j]},
    t[i][j] = 0 if a[i] = b[j] else t[i][j] = 1,   i=1,2,...,n;  j=1,2,...,m
    m[0][j] = j
    m[i][0] = i

    Args:
        a: sequence a
        b: sequence b
        show_opt: whether to show the operations that change a to b or not. Default is false.
                  Note that the operations are not unique, we only show one of them.

    Returns:
        an integer of minimal edit distance
    """
    m_edit = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0:
                m_edit[i][j] = j
            elif j == 0:
                m_edit[i][j] = i
            else:
                e1 = m_edit[i - 1][j] + 1
                e2 = m_edit[i][j - 1] + 1
                e3 = m_edit[i - 1][j - 1] + int(a[i - 1] != b[j - 1])
                m_edit[i][j] = min([e1, e2, e3])
    if show_opt == True:
        opt_list = []
        while True:
            if i == j == 0:
                break
            if i == 0:
                opt_list.insert(0, 'insert ' + b[:j])
                break
            if j == 0:
                opt_list.insert(0, 'delete ' + a[:i])
                break
            e1 = m_edit[i - 1][j] + 1
            e2 = m_edit[i][j - 1] + 1
            e3 = m_edit[i - 1][j - 1] + int(a[i - 1] != b[j - 1])
            if e1 == m_edit[i][j]:
                opt_list.insert(0, 'delete ' + a[i - 1])
                i = i - 1
            elif e2 == m_edit[i][j]:
                opt_list.insert(0, 'insert ' + b[j - 1])
                j = j - 1
            else:
                if a[i - 1] == b[j - 1]:
                    opt_list.insert(0, 'equal ' + a[i - 1])
                else:
                    opt_list.insert(0, 'replace ' + a[i - 1] + ' with ' + b[j - 1])
                i = i - 1
                j = j - 1
        print ' -> '.join(opt_list)
    return m_edit[len(a)][len(b)]


def lcs(a, b, show_lcs=False):
    """Compute the longest common subsequence(lcs) of sequence a and b.

    For example, a=['a', 'b', 'c', 'b', 'd', 'a', 'b'], b=['b', 'd', 'c', 'a', 'b', 'a'],
    one of their longest common subsequence is ['b', 'c', 'a', 'b'], the length of
    their longest common subsequence is 4. The longest common subsequence may not be 
    continuous in the original sequence.

    Args:
        a: sequence a
        b: sequence b
        show_lcs: whether to show one of the longest common subsequence of sequence a and b or not.

    Returns:
        the length of the longest common subsequence.
    """
    m_lcs = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i * j == 0:
                m_lcs[i][j] = 0
            else:
                if a[i - 1] == b[j - 1]:
                    m_lcs[i][j] = m_lcs[i - 1][j - 1] + 1
                else:
                    m_lcs[i][j] = max(m_lcs[i - 1][j], m_lcs[i][j - 1])
    if show_lcs:
        lcs_list = []
        while True:
            if i * j == 0:
                break
            else:
                if a[i - 1] == b[j - 1]:
                    lcs_list.insert(0, a[i - 1])
                    i = i - 1
                    j = j - 1
                else:
                    if m_lcs[i - 1][j] >= m_lcs[i][j - 1]:
                        i = i - 1
                    else:
                        j = j - 1
        print ''.join(lcs_list)
    return m_lcs[len(a)][len(b)]


def lccs(a, b, show_lccs=False):
    """Compute the longest common continuous subsequence(lccs) of sequence a and b.

    For example, a=['a', 'b', 'c', 'd', 'a', 'f', 'g'],
    b=['c', 'b', 'a', 'c', 'd', 'a', 'f', 'a', 'f', 'g'], one of their longest common 
    continuous subsequence is ['c', 'd', 'a', 'f']. The longest common continuous subsequence
    must be continuous in a and b.

    Args:
        a: sequence a
        b: sequence b
        show_lccs: whether to show one of the longest common continuous subsequence 
                   of sequence a and b or not.

    Returns:
        the length of the longest common continuous subsequence.
    """
    v_lccs = 0
    i_lccs = 0
    m_lccs = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i * j == 0:
                m_lccs[i][j] = 0
            else:
                if a[i - 1] == b[j - 1]:
                    m_lccs[i][j] = m_lccs[i - 1][j - 1] + 1
                else:
                    m_lccs[i][j] = 0
                if m_lccs[i][j] > v_lccs:
                    v_lccs = m_lccs[i][j]
                    i_lccs = i - 1
    if show_lccs:
        print a[i_lccs - v_lccs + 1:i_lccs + 1]
    return v_lccs


def sw(a, b, show_align=False, match_score=2, mismatch_score=-2, gap_score=-1):
    """Implementation of Smith-Waterman algorithm(sw).

    The Smith-Waterman algorithm performs local sequence alignment, that is, 
    for determining similar regions between two sequence. For details, see:
    https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm

    Args:
        a: sequence a.
        b: sequence b.
        show_align: whether to show the alignment(based on Smith-Waterman algorithm) 
                    between sequence a and b or not. Note that the alignment may not
                    be unique, we only show one of them.
        match_score: match score, default is 2.
        mismatch_score: mismatch score, default is -2.
        gap_score: gap penalty, default is -1.

    Returns:
        The overall score of the alignment(based on Smith-Waterman algorithm).
    """
    m_sw = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i * j == 0:
                m_sw[i][j] = 0
            else:
                align1 = m_sw[i - 1][j] + gap_score
                align2 = m_sw[i][j - 1] + gap_score
                align3 = m_sw[i - 1][j - 1] + \
                            (match_score if a[i - 1] == b[j - 1] else mismatch_score)
                m_sw[i][j] = max([0, align1, align2, align3])
    if show_align:
        a_align = []
        b_align = []
        while True:
            if m_sw[i][j] == 0:
                a_align = list(a[:i]) + a_align
                b_align = list(b[:j]) + b_align
                if len(a_align) > len(b_align):
                    b_align = ['-'] * (len(a_align) - len(b_align)) + b_align
                else:
                    a_align = ['-'] * (len(b_align) - len(a_align)) + a_align
                break
            align1 = m_sw[i - 1][j] + gap_score
            align2 = m_sw[i][j - 1] + gap_score
            align3 = m_sw[i - 1][j - 1] + \
                        (match_score if a[i - 1] == b[j - 1] else mismatch_score)
            if m_sw[i][j] == 0:
                continue
            elif m_sw[i][j] == align3:
                a_align.insert(0, a[i - 1])
                b_align.insert(0, b[j - 1])
                i = i - 1
                j = j - 1
            elif m_sw[i][j] == align1:
                a_align.insert(0, a[i - 1])
                b_align.insert(0, '-')
                i = i - 1
            elif m_sw[i][j] == align2:
                a_align.insert(0, '-')
                b_align.insert(0, b[j - 1])
                j = j - 1
        print a_align
        print b_align
    return m_sw[len(a)][len(b)]
