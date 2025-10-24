import marimo

__generated_with = "0.16.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import requests
    from urllib.parse import urlencode
    from lxml import etree
    import xml.etree.ElementTree as ET
    import pandas as pd
    import unicodedata
    return etree, mo, pd, requests, urlencode


@app.cell
def _(mo):
    mo.md(
        r"""
    # Einführung in die OAI-Schnittstelle der Digitalisierten Sammlungen der Stabi Berlin

    ## Abrufen aller verfügbaren Sets
    """
    )
    return


@app.cell
def _(mo):
    # define switch for base-URLs
    base_URL = mo.ui.dropdown(options={"Digitalisierte Sammlungen Stabi Berlin": "https://oai.sbb.berlin/"}, value="Digitalisierte Sammlungen Stabi Berlin", label="Base-URL")
    return (base_URL,)


@app.cell
def _(base_URL):
    base_URL
    return


@app.cell
def _(base_URL):
    base_url = base_URL.value
    ns = {"oai": "http://www.openarchives.org/OAI/2.0/",
         "dc": "http://purl.org/dc/elements/1.1/"}
    return base_url, ns


@app.cell
def _(base_url, etree, ns, pd, requests, urlencode):
    def get_sets():

        resumption_token = None
        sets=[]
        while True:

            if resumption_token:
                params = {'verb': 'ListSets', 'resumptionToken': resumption_token}
            else:
                params = {'verb': 'ListSets'}

            query_string = urlencode(params, safe='+')
            response = requests.get(base_url + '?' + query_string)
            content = response.content

            parser = etree.XMLParser(recover=True)
            root = etree.fromstring(content, parser)



            for set_el in root.findall('.//oai:set', ns):
                spec_el = set_el.find('oai:setSpec', ns)
                name_el = set_el.find('oai:setName', ns)
                set_spec = spec_el.text.strip() if spec_el is not None and spec_el.text else ''
                set_name = name_el.text.strip() if name_el is not None and name_el.text else ''
                sets.append({'setSpec': set_spec, 'setName': set_name})

            rt_el = root.find('.//oai:resumptionToken', ns)
            resumption_token = rt_el.text.strip() if rt_el is not None and rt_el.text and rt_el.text.strip() else None

            if not resumption_token:
                break  # no more pages

        df = pd.DataFrame(sets)
        # add index column for easier selection
        df.reset_index(drop=False, inplace=True)
        df.rename(columns={'index': 'idx'}, inplace=True)
        return df
    return (get_sets,)


@app.cell
def _(get_sets):
    df_sets = get_sets()
    df_sets
    return (df_sets,)


@app.cell
def _(base_url, etree, ns, requests, urlencode):
    def get_nr_of_records(set):
        params = {"verb": "ListIdentifiers",
                  "metadataPrefix": "oai_dc",
                  "set": set
                 }
        query_string = urlencode(params, safe='+')
        response = requests.get(base_url + '?' + query_string)
        content = response.content
        parser = etree.XMLParser(recover=True)
        root = etree.fromstring(content, parser)
        print(response.url)	
        rt_el = root.find('.//oai:resumptionToken', ns)
        if rt_el is not None:
            nr_of_recs = rt_el.get('completeListSize')
        else:
            nr_of_recs = len(root.findall('.//oai:header', ns))
        return int(nr_of_recs)

    return (get_nr_of_records,)


@app.cell
def _(mo):
    mo.md(r"""## Abrufen der Zahl der pro Set verfügbaren Records""")
    return


@app.cell
def _(mo):
    set_to_get = mo.ui.text(label="setSpec eingeben:")

    button_get = mo.ui.run_button(label="Hole Zahl der records für dieses Set")
    #button_all = mo.ui.run_button(label="Hole Zahl der records für alle Sets")
    return button_get, set_to_get


@app.cell
def _(button_get, mo, set_to_get):
    mo.hstack([set_to_get, button_get])
    #mo.vstack([mo.hstack([set_to_get, button_get]), button_all])
    return


@app.cell
def _(button_get, df_sets, get_nr_of_records, set_to_get):
    #if button_all.value:
        #df_sets['Nr_of_records'] = df_sets['setSpec'].apply(get_nr_of_records)
    if button_get.value:
        mask = df_sets['setSpec'] == set_to_get.value
        df_sets.loc[mask, 'Nr_of_records'] = df_sets.loc[mask, 'setSpec'].apply(get_nr_of_records)
    return


@app.cell
def _(button_get, df_sets, mo):
    mo.stop(not button_get.value)
    df_sets
    return


@app.cell
def _(button_get, button_get_50, mo):
    mo.stop(not(button_get.value or button_get_50.value))
    mo.md("## Abrufen der Records")
    return


@app.cell
def _(mo):
    get_recs = mo.ui.text(label="setSpec eingeben:")

    button_get_all = mo.ui.run_button(label="Hole alle records in diesem Set")
    button_get_50 = mo.ui.run_button(label="Hole die ersten 50 records in diesem Set")
    return button_get_50, button_get_all, get_recs


@app.cell
def _(button_get, button_get_50, button_get_all, get_recs, mo):
    mo.stop(not(button_get.value or button_get_50.value))
    mo.vstack([get_recs, mo.hstack([
    button_get_50, button_get_all])])
    return


@app.cell
def _(base_url, etree, ns, requests, urlencode):
    def get_records(set, limit):

        resumption_token = None
        rec_els=[]
        while True:

            if resumption_token:
                params = {"verb": "ListRecords",
                  'resumptionToken': resumption_token}
            else:
                params = {"verb": "ListRecords",
                  "metadataPrefix": "oai_dc",
                  "set": set}

            query_string = urlencode(params, safe='+')
            response = requests.get(base_url + '?' + query_string)
            print(response.url)	
            content = response.content

            parser = etree.XMLParser(recover=True)
            root = etree.fromstring(content, parser)



            for rec_el in root.findall('.//oai:record', ns):
                rec_els.append(rec_el)

            rt_el = root.find('.//oai:resumptionToken', ns)
            resumption_token = rt_el.text.strip() if rt_el is not None and rt_el.text and rt_el.text.strip() else None

            if not resumption_token or limit:
                break  # no more pages

        return rec_els
    return (get_records,)


@app.cell
def _(button_get_50, button_get_all, get_records, get_recs, parse_records):
    if button_get_50. value:
        records_parsed = parse_records(get_records(get_recs.value, True))
    if button_get_all. value:
        records_parsed = parse_records(get_records(get_recs.value, False))
    return (records_parsed,)


@app.cell
def _(etree, pd):
    def parse_records(records):
        all_data = []

        for record in records:
            data = {}

            # ---- Header fields ----
            header = record.find('header')
            if header is not None:
                data['header_identifier'] = header.findtext('identifier')
                data['header_datestamp'] = header.findtext('datestamp')
                set_specs = [el.text for el in header.findall('setSpec') if el.text]
                if set_specs:
                    data['header_setSpec'] = set_specs

            # ---- Metadata fields ----
            dc_container = record.find('.//{http://www.openarchives.org/OAI/2.0/oai_dc/}dc')
            if dc_container is not None:
                for child in dc_container:
                    tag = etree.QName(child).localname
                    key = f'dc_{tag}'
                    if child.text:
                        data.setdefault(key, []).append(child.text)

            all_data.append(data)

        # combine all parsed records into one DataFrame
        df = pd.DataFrame(all_data)
        return df
    return (parse_records,)


@app.cell
def _(records_parsed):
    records_parsed
    return


@app.cell
def _(records_parsed):
    records_parsed["image_url"] = records_parsed["dc_identifier"].apply(
        lambda lst: next(
            (
                f"https://content.staatsbibliothek-berlin.de/dc/{x}-00000001/full/full/0/default.jpg"
                for x in lst if isinstance(x, str) and x.startswith("PPN")
            ),
            None
        )
    )
    return


@app.cell
def _(images, mo):
    mo.stop(not images)
    mo.md("## Abrufen des jeweils ersten Bildes pro record (über IIIF)")
    return


@app.cell
def _(mo, records_parsed):
    # Create marimo image UI elements
    images = [mo.image(src=url, width=200, height=200) for url in records_parsed["image_url"]]

    # Display as a responsive gallery
    gallery = mo.hstack(images, wrap=True, gap="1rem")
    gallery
    return (images,)


if __name__ == "__main__":
    app.run()
