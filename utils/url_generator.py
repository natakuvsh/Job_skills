
def generate_url(search_term, page):
    """
    Generating the search url
    """
    base_template = 'https://www.work.ua/jobs-{}/'
    search_term = search_term.replace(' ', '+')
    stem = base_template.format(search_term)
    url_template = stem + '?page={}f'
    if page == 1:
        return stem
    else:
        return url_template.format(page)