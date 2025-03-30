""" zid_project1.py

"""
import json
import os

import toolkit_config as cfg

# ----------------------------------------------------------------------------
# Location of files and folders
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' strings with the appropriate
#   expressions.
# IMPORTANT:
#   - Use the appropriate method from the `os` module to combine paths
#   - Do **NOT** include full paths like "C:\\User...". You **MUST* combine
#     paths using methods from the `os` module
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
ROOTDIR = os.path.join(cfg.PRJDIR, "project1")
DATDIR = os.path.join(ROOTDIR, "data")
TICPATH = os.path.join(ROOTDIR, "TICKERS.txt")
# ----------------------------------------------------------------------------
# Variables describing the contents of ".dat" files
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' string with the appropriate
#     expression.
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
# NOTE: `COLUMNS` must be a list, where each element is a column name in the
# order they appear in the ".dat" files
COLUMNS = ["Volume", "Date", "Adj Close", "Close", "Open", "High"]

# NOTE: COLWIDTHS must be a dictionary with {<col> : <width>}, where
# - Each key (<col>) is a column name in the `COLUMNS` list
# - Each value (<width>) is an **integer** with the width of the column, as
#   defined in your README.txt file
#
COLWIDTHS = {"Volume":14,
             "Date": 11,
             "Adj Close": 19,
             "Close": 10,
             "Open": 6,
             "High": 20}


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def get_tics(pth):
    """ Reads a file containing tickers and their corresponding exchanges.
    Each non-empty line of the file is guaranteed to have the following format:

    "XXXX"="YYYY"

    where:
        - XXXX represents an exchange.
        - YYYY represents a ticker.

    This function should return a dictionary, where each key is a properly formatted
    ticker, and each value the properly formatted exchange corresponding to the ticker.

    Parameters
    ----------
    pth : str
        Full path to the location of the TICKERS.txt file.

    Returns
    -------
    dict
        A dictionary with format {<tic> : <exchange>} where
            - Each key (<tic>) is a ticker found in the file specified by pth (as a string).
            - Each value (<exchange>) is a string containing the exchange for this ticker.

    Notes
    -----
    The keys and values of the dictionary returned must conform with the following rules:
        - All characters are in lower case
        - Only contain alphabetical characters, i.e. does not contain characters such as ", = etc.
        - No spaces
        - No empty tickers or exchanges

    """
    dict = {}
    with open(pth) as file:
        for line in file:
            exchange,ticker = [i.lower() for i in line.strip().replace('"', '').split("=")]
            dict[ticker] = exchange
            # dict[line.strip().replace('"','').split("=")[::-1][0].lower()] = line.strip().replace('"','').split("=")[::-1][1].lower()
    return dict

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def read_dat(tic):
    """ Returns a list with the lines of the ".dat" file containing the stock
    price information for the ticker `tic`.


    Parameters
    ----------
    tic : str
        Ticker symbol, in lower case.

    Returns
    -------
    list
        A list with the lines of the ".dat" file for this `tic`. Each element
        is a line in the file, without newline characters (e.g. '\n')


    Hints (optional)
    ----------------
    - Create a variable with the location of the relevant file using the `os`
      module, the `DATDIR` constant, and f-strings.

    """
    # IMPORTANT: The answer to this question should NOT include full paths
    # like "C:\\Users...". There should be no forward or backslashes.
    line_list = []
    with open(os.path.join(DATDIR, "{}_prc.dat".format(tic))) as file:
        for line in file:
            line_list.append(line.strip())

    return line_list

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def line_to_dict(line):
    """Returns the information contained in a line of a ".dat" file as a
    dictionary, where each key is a column name and each value is a string
    with the value for that column.

    This line will be split according to the field width in `COLWIDTHS`
    of each column in `COLUMNS`.

    Parameters
    ----------
    line : str
        A line from ".dat" file, without any newline characters

    Returns
    -------
    dict
        A dictionary with format {<col> : <value>} where
        - Each key (<col>) is a column in `COLUMNS` (as a string)
        - Each value (<value>) is a string containing the correct value for
          this column.

    Hints (optional)
    ----------------
    - Your solution should include the constants `COLUMNS` and `COLWIDTHS`
    - For each line in the file, extract the correct value for each column
      sequentially.

    """
    dict = {}
    index = 0
    for i in COLUMNS:
        dict[i] = line[index:index+COLWIDTHS[i]].replace(" ", "")
        index += COLWIDTHS[i]
    return dict

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_tickers(tic_exchange_dic, tickers_lst=None):
    """Verifies if the tickers provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        tic_exchange_dic : dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If tickers_lst is not None, raise an Exception if any of the below rules are violated:
            1. tickers_lst is an empty list.

            2. tickers_lst contains a ticker that does not correspond to a key tic_exchange_dic

               Example:
               If tic_exchange_dic is {'tsm':'nyse', 'aal':'nasdaq'},
               tickers_lst = ['aal', 'Tsm'] would raise an Exception because
               'Tsm' is not a key of tic_exchange_dic.

    """
    # if tickers_lst is not None and tickers_lst == []:
    if tickers_lst == []:
        raise Exception("tickers_lst is empty!")
    elif tickers_lst != []:
        for item in tickers_lst:
            if item not in tic_exchange_dic:
                raise Exception(f"{item} in tickers_lst is not a item of tic_exchange_dic.")

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_cols(col_lst=None):
    """Verifies if the column names provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        col_lst : list, optional
            A list containing column names (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If col_lst is not None, raise an Exception if any of the below rules are violated:
            1. col_lst is an empty list.

            2. col_lst contains a column that is not found in `COLUMNS`.

               Example:
               If COLUMNS = ['Close', 'Date'],
               col_lst = ['close'] would raise an Exception because 'close' is not found in `COLUMNS`

    """
    # if col_lst is not None and col_lst == []:
    if col_lst == []:
        raise Exception("col_lst is empty!")
    elif col_lst != []:
        for item in col_lst:
            if item not in COLUMNS:
                raise Exception(f"{item} in col_lst is not found in COLUMNS.")

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    """Returns a dictionary containing the data for the tickers specified in tickers_lst.
        An Exception is raised if any of the tickers provided in tickers_lst or any of the
        column names provided in col_lst are invalid.

        Parameters
        ----------
        tic_exchange_dic: dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings)

        col_lst : list, optional
            A list containing column names (as strings)

        Returns
        -------
        dict
            A dictionary with format {<tic> : <data>} where
            - Each key (<tic>) is a ticker in tickers_lst (as a string)
            - Each value (<data>) is a dictionary with format
                {
                    'exchange': <tic_exchange>,
                    'data': [<dict_0>, <dict_1>, ..., <dict_n>]
                }
              where
                - <tic_exchange> refers to the exchange that <tic> belongs to in lower case.
                - <dict_0> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[0]),
                  but that only contains the columns listed in col_lst
                - <dict_n> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[-1]),
                  but that only contains the columns listed in col_lst

        Notes
        -----
        - Please refer to the assessment description for an example of what the returned dictionary should look like.
        - If tickers_lst is None, the dictionary returned should contain the data for
          all tickers found in tic_exchange_dic.
        - If col_lst is None, <dict_0>, <dict_1>, ... should contain all the columns found in `COLUMNS`

        Hints (optional)
        ----------------
        - To check if tickers_lst contains any invalid tickers, you can call `verify_tickers`
        - To check if col_lst contains any invalid column names, you can call `verify_cols`
        - This function should call the `read_dat` and `line_to_dict` functions

    """
    dict = {}
    tics = sorted(tic_exchange_dic.keys())

    if tickers_lst is None:
        tickers_lst = tics
    else:
        verify_tickers(tic_exchange_dic, tickers_lst)

    if col_lst is not None:
        verify_cols(col_lst)

    for t in tickers_lst:
        ticker_data = [line_to_dict(line) for line in read_dat(t)]

        if col_lst is not None:
            ticker_data = [{col: data[col] for col in col_lst} for data in ticker_data]#！！！！

        dict[t] = {"exchange": tic_exchange_dic[t], "data": ticker_data}

    # if tickers_lst is None and col_lst is None:
    #     for t in tics:
    #         ticker_data = []
    #         for line in read_dat(t):
    #             ticker_data.append(line_to_dict(line))
    #         dict[t] = {"exchange": tic_exchange_dic[t], "data": ticker_data}
    # elif tickers_lst is None and col_lst is not None:
    #     verify_cols(col_lst)
    #     for t in tics:
    #         ticker_data = []
    #         for line in read_dat(t):
    #             for col in col_lst:
    #                 ticker_data.append({col:line_to_dict(line)[col]})
    #         dict[t] = {"exchange": tic_exchange_dic[t], "data": ticker_data}
    # elif tickers_lst is not None and col_lst is None:
    #     verify_tickers(tic_exchange_dic, tickers_lst)
    #     for t in tickers_lst:
    #         ticker_data = []
    #         for line in read_dat(t):
    #             ticker_data.append(line_to_dict(line))
    #         dict[t] = {"exchange": tic_exchange_dic[t], "data": ticker_data}
    # else:
    #     verify_tickers(tic_exchange_dic, tickers_lst)
    #     verify_cols(col_lst)
    #     for t in tickers_lst:
    #         ticker_data = []
    #         for line in read_dat(t):
    #             for col in col_lst:
    #                 ticker_data.append({col:line_to_dict(line)[col]})
    #         dict[t] = {"exchange": tic_exchange_dic[t], "data": ticker_data}

    return dict

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_json(data_dict, pth):
    """Saves the data found in the data_dict dictionary into a
        JSON file whose name is specified by pth.

        Parameters
        ----------
        data_dict: dict
            A dictionary returned by the `create_data_dict` function

        pth : str
            The complete path to the output JSON file. This is where the file with
            the data will be saved.


        Returns
        -------
        None
            This function does not return anything

    """
    with open(pth, "w") as json_file:
        json.dump(data_dict, json_file, indent=4)

# ----------------------------------------------------------------------------
#    Please put your answers for the open questions here:
# ----------------------------------------------------------------------------
    """
Open-ended question A:
(1)Using OS packages instead of absolute paths for path configuration is because it allows the code to have good transferability.Different computer operating systems have different file path separators.If an absolute path is used, the code may encounter errors on different operating systems. Using os.path.join() can automatically use the correct path delimiter according to the requirements of the operating system.In addition, even with the same operating system, absolute paths often become invalid when moving projects from one machine to another or from one directory to another. Using relative paths, no matter where the project is moved, as long as the relative position of the file remains unchanged, the path remains valid.Finally, using os.path.join() can ensure clear path construction, especially when the path contains multiple levels.In this way,the construction logic of the path becomes more modular and maintainable.

(2)Hypotheses 2 is more likely to be true.
 For Hypothesis 1, articles reflect investors' evaluations, which means that the journalist's article only reflects the current investor sentiment (which this sentiment has already been reflected in the stock price). However, if only reporting existing investor sentiment, prices may experience a reversal in the long run, as short-term price changes based on investor sentiment typically correct over time, which is known as mean reversion of stock prices. This is inconsistent with the observed phenomenon.

 For Hypothesis 2,the journalist provided valuable information beyond firm fundamentals.Based on the observed phenomenon, it indicates that the information provided by the journalist is not only a reflection of investor sentiment, but also provides information with independent predictive ability. If the reporter includes information that has not yet been fully reflected in the stock price in the article, this negative sentiment will continue to affect stock returns in a sustained manner, thereby causing an impact on long-term stock prices, which is consistent with the phenomenon we have observed. If the information is incorrect or only an emotional response, there will be a mean regression of the stock price.

(3)We can predict that trading volume will increase in the short term. Under hypothesis 2, the journalist provides valuable new negative information beyond the fundamentals, which raises concerns among investors about the uncertainty of their stock price and leads to wise trading (for example, some investors see this negative news as a sell signal), increasing trading volume. Even if investors do not have homogeneous expectations for this information, some investors may overreact, further driving an increase in trading volume. In addition, as the article evolves, more and more investors are paying attention to this information and participating in trading (this will also increase trading volume). At this time, institutional algorithms (such as emotion tracking algorithms) may use real-time price changes for speculative trading, further amplifying short-term trading volume.

Open-ended question B:
(1)Bloomberg, The Wall Street Journal(WSJ), Reuters

(2)The three media sources are likely both substitutable and complementary, depending on the context of their coverage. If all three media outlets report the same event with similar emotions (such as earnings announcements, mergers), investors can use any of them interchangeably. This indicates that they are substitutable. At the same time, each media outlet can provide unique insights or exclusive news about a particular stock, so using multiple media sources together can provide a more complete understanding of the company, which means they are complementary. For example, Bloomberg provides institutional level analysis and forward-looking indicators, WSJ is better at delving into corporate governance and strategy, and Reuters focuses more on fact driven global reporting. In addition, Bloomberg's target is professional investors, which may lead to faster price responses, while WSJ and Reuters cater to a wider audience, which may lead to slower price responses. We can choose the corresponding media according to our own needs.

I use the Vector Autoregression (VAR) model to test the relationship between them. The VAR model is very useful because it can capture the dynamic relationships between multiple time series variables. In this case, we can use VAR to examine whether the emotions of one media source affect or are influenced by the emotions of other media sources over time. The model is defined as follows：

            𝐒_Bloomberg,t = α₁ + ∑β₁₁,ₖ 𝐒_Bloomberg,t₋ₖ + ∑β₁₂,ₖ 𝐒_Reuters,t₋ₖ + ∑β₁₃,ₖ 𝐒_WSJ,t₋ₖ + ϵ₁,t
            𝐒_Reuters,t = α₂ + ∑β₂₁,ₖ 𝐒_Bloomberg,t₋ₖ + ∑β₂₂,ₖ 𝐒_Reuters,t₋ₖ + ∑β₂₃,ₖ 𝐒_WSJ,t₋ₖ + ϵ₂,t
            𝐒_WSJ,t = α₃ + ∑β₃₁,ₖ 𝐒_Bloomberg,t₋ₖ + ∑β₃₂,ₖ 𝐒_Reuters,t₋ₖ + ∑β₃₃,ₖ 𝐒_WSJ,t₋ₖ + ϵ₃,t
            
    Where:
         𝐒_Bloomberg,t : Bloomberg's emotional score at time t
         𝐒_Reuters,t : Reuters' emotional score at time t
         𝐒_WSJ,t : WSJ's emotional score at time t'
         α₁, α₂, α₃ : Intercept
         βᵢⱼ,ₖ : The coefficient of influence of variable j on variable i during the lag period k, which means it measures the effect of sentiment from source j on source i over lag k(For example, if β₁₂,ₖ and β₁₃,ₖ are significant, it suggests that Bloomberg is influenced by Reuters and WSJ, indicating complementarity.If the coefficients on other sources’ sentiment are small or insignificant, it suggests the sources are substitutes, as they do not strongly depend on each other.)
         ϵ₁, ϵ₂, ϵ₃ : Error term

Interpretation of Results: If cross-source coefficients βᵢⱼ,ₖ are large and significant, shows news sentiment is interdependent, which means that the sources of information are complementary (they influence each other and provide additional insights); If they are small or insignificant, this means the sources are largely independent, implying that they are substitutes (each can stand alone without relying on the others). Finally, Impulse Response Functions (IRFs) can also be used to examine how emotional shocks from one source affect other sources over time, in order to further understand complementarity or substitutability.

My prediction: Bloomberg and Reuters may be more substitutable as they both focus on real-time financial news, while The Wall Street Journal may be more complementary as it provides deeper analysis and opinion articles that Bloomberg and Reuters may not have covered.

(3)
 How can I make sure an article is accurate
1.Through cross validation of authoritative media sources: Compare the key data in the article with other independent and authoritative public information, such as company financial reports and government statistical data. This direct comparison with the original data avoids bias in the transmission of information. For example, if an article claims that a company's quarterly revenue has increased by 50%, then go to its official website to search for official financial reports or third-party audit reports.

2.Check references and raw data: If the article indicates the citation source of the data, it is necessary to clarify whether the citation source is traceable, such as from research reports or expert interviews. By tracing the source of information through reference chains, transparency can be enhanced.

3.Evaluate the credibility of the author and the publishing platform: We need to ensure that the platform for publishing articles is reliable and that the authors have a professional background in the relevant field. For example, is the platform for publishing articles a personal website or a government website? Does the author have any professional experience? For Bloomberg, their financial analysis team's article is more convincing because they are very professional.

4.Logical consistency check: Check if the logical coherence of the viewpoints before and after the article, and analyze if there are any contradictory statements within the article. For example, if someone claims that "the company's cash flow is healthy" earlier, but later claims that "emergency financing is needed," then it is necessary to be skeptical of this article

 when it is impossible to justify it?
1.Original data missing: When it comes to undisclosed internal data (such as financial details of private enterprises), such as an article citing "anonymous executive disclosure," but the company has not publicly responded, this will result in unverifiable information.

2.Sudden events or dynamic information: In the early stages of a major event, information is fragmented and rapidly changing, and early reports often contain errors. This is because at this time, people have not yet seen the full picture of the situation, their speculative views are often inaccurate, and there is no verifiable data. So we (as readers) also cannot judge the accuracy of a certain article very well. For example, in the early stages of the 2010 US stock market crash, there were various speculations from the media about the cause, and it was only later confirmed as an algorithmic trading issue.

3.Involving highly specialized or technical content: When it comes to cutting-edge technologies such as complex derivative pricing, biomedicine, and artificial intelligence, if we are not experts in these areas, we cannot judge the accuracy and credibility of an article very well.

4.Deliberately fabricated false information: If an article uses deepfakes, forged documents, or fabricated sources (such as false "experts") to confuse the public, we cannot accurately judge its accuracy. For example, in the 2021 GameStop incident, a large number of misleading screenshots circulated on social media, affecting market sentiment.

5.Mixed viewpoints and facts: Selective selection of objective facts and the author's own viewpoints mixed together to express, which readers easily believe as facts (advanced brainwashing method). For example, an article provides traceable data (which is a few bad data specifically selected from a large amount of good data) and claims that a company has "failed management". If readers do not have a complete understanding of the overall data, it is easy to believe such statements easily
(We can use the following methods to avoid the above situation: first, clearly distinguish verified information from unverified information (such as using footnotes to indicate that "data sources have not been independently verified"), then give higher weight to high credibility media (such as The Wall Street Journal) to reduce the impact of low credibility sources, and finally, combine multiple similar reports to indirectly infer accuracy through consensus (such as 80% of articles stating the same viewpoint).)
    """


def _test_create_json(json_pth):
    """ Test function for the `create_json_ function.
    This function will save the dictionary returned by `create_data_dict` to the path specified.

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    # tickers_lst = ["aapl"]
    # col_lst = ["Date","Volume"]
    data_dict = create_data_dict(tic_exchange_dic,["csco"])
    create_json(data_dict, json_pth)
    print(f'Data saved to {json_pth}')


# ----------------------------------------------------------------------------
#  Uncomment the statements below to call the test and/or main functions.
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Test functions
    # _test_get_tics()
    # _test_read_dat()
    # _test_line_to_dict()
    # _test_create_data_dict()
    _test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json
    pass
