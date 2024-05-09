import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def display_metrics_table(models, precision, recall, f1_score, roc_auc, accuracy):
    data = {
        'Model': models,
        'Precision': precision,
        'Recall': recall,
        'F1-score': f1_score,
        'ROC AUC': roc_auc,
        'Accuracy': accuracy
    }
    df = pd.DataFrame(data)
    st.table(df.style.set_caption("Model Performance Metrics").set_properties(**{'text-align': 'center'}))

def plot_comparison(models, metric, values, xlabel):
    fig = go.Figure(data=[
        go.Bar(name='XGBoost', x=models, y=values[0]),
        go.Bar(name='CatBoost', x=models, y=values[1])
    ])
    fig.update_layout(barmode='group', xaxis_title='Models', yaxis_title=xlabel,
                      title=f'{metric} Comparison')
    st.plotly_chart(fig)

def app():
    st.title("Model Performance Metrics")

    # Model performance data
    models = ["XGBoost", "CatBoost"]
    precision = [[0.9613], [0.9621]]
    recall = [[0.9752], [0.9797]]
    f1_score = [[0.9682], [0.9709]]
    roc_auc = [[0.9629], [0.9656]]
    accuracy = [[0.9643], [0.9672]]

    # Display metrics in a table
    display_metrics_table(models, precision, recall, f1_score, roc_auc, accuracy)

    # Plot accuracy comparison
    plot_comparison(models, 'Accuracy', accuracy, 'Accuracy')

    # Plot precision comparison
    plot_comparison(models, 'Precision', precision, 'Precision')

    # Plot recall comparison
    plot_comparison(models, 'Recall', recall, 'Recall')

    # Plot F1-score comparison
    plot_comparison(models, 'F1-score', f1_score, 'F1-score')

    # Plot ROC AUC comparison
    plot_comparison(models, 'ROC AUC', roc_auc, 'ROC AUC')

if __name__ == "__main__":
    app()
