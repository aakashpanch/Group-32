# import random
import uuid
from Model import metamodel_dict
import streamlit as st
import json
#import graphviz
from streamlit_agraph import agraph, Node, Edge, Config
import networkx as nx
from graph_functions import output_nodes_and_edges, count_nodes, count_edges
from streamlit_option_menu import option_menu
from st_btn_select import st_btn_select
from tabs import (upload_graph, create_node, create_relation, store_graph, visualization_graph, analyze_graph,
                  export_graph)

if __name__ == '__main__':
    if "node_list" not in st.session_state:
        st.session_state["node_list"] = []
    # if "node_list1" not in st.session_state:  # node_list1 - data from imported JSON file
    # st.session_state["node_list1"] = []
    if "edge_list" not in st.session_state:
        st.session_state["edge_list"] = []
    # if "edge_list1" not in st.session_state:  # edge_list1 - data from imported JSON file
    #  st.session_state["edge_list1"] = []
    if "graph_dict" not in st.session_state:
        st.session_state["graph_dict"] = []

    tab_list = [
            "import existing graph",
            "Create Nodes (Nodes)",
            "Create Relation",
            "Store the graph",
            "Visualize the graph",
            "Analyze the graph",
            "Export the graph"
        ]

    st.set_page_config(layout="wide")
    with st.sidebar:
        selected_tab = option_menu("Main Menu",
                                   tab_list,
                                   icons=['house', 'gear', 'arrow-clockwise', 'apple', 'asterisk', 'balloon',
                                          'boombox'],
                                   menu_icon="cast",
                                   default_index=0,
                                   orientation="vertical"
                                   )

    #selected_tab = option_menu("Main Menu",
                          #     tab_list,
                        #       icons=['house', 'gear', 'arrow-clockwise','apple','asterisk','balloon','boombox'],
                         #      menu_icon="cast",
                          #     default_index=1,
                          #     orientation= "horizontal"
                           #    )
    st.write(selected_tab)

    st.title("PyINPSE Tutorial 1")

    if selected_tab == "import existing graph":
        upload_graph()

    if selected_tab == "Create Nodes (Nodes)":
        create_node()

    if selected_tab ==  "Create Relation":
        create_relation()

    if selected_tab == "Store the graph":
        store_graph()

    if selected_tab ==  "Visualize the graph":
        visualization_graph()

    if selected_tab ==  "Analyze the graph":
        analyze_graph()

    if selected_tab ==  "Export the graph":
        export_graph()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
