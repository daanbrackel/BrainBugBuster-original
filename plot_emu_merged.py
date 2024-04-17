import argparse
import pandas as pd
import plotly.graph_objects as go

def plot_abundance(input_csv, output_species_html, output_genus_html):
    # Read input CSV
    df = pd.read_csv(input_csv)

    # Species plot
    species_df = df.drop(columns=['genus'])  # Drop genus column
    species_df['abundance'] *= 100  # Multiply abundance by 100 to get percentage
    species_df['genus'] = species_df['species']  # Rename species column to genus for consistency
    species_df.drop(columns=['species'], inplace=True)  # Drop species column
    species_df_grouped = species_df.groupby(['Barcode', 'genus']).sum().reset_index()

    # Aggregate species with <1% abundance into 'Other species <1%'
    species_df_grouped.loc[species_df_grouped['abundance'] < 1, 'genus'] = 'Other species <1%'
    species_df_grouped = species_df_grouped.groupby(['Barcode', 'genus']).sum().reset_index()
    species_pivot_table = species_df_grouped.pivot(index='Barcode', columns='genus', values='abundance').fillna(0)

    # Genus plot
    genus_df = df.drop(columns=['species'])  # Drop species column
    genus_df['abundance'] *= 100  # Multiply abundance by 100 to get percentage
    genus_df_grouped = genus_df.groupby(['Barcode', 'genus']).sum().reset_index()

    # Aggregate genera with <1% abundance into 'Other genera <1%'
    genus_df_grouped.loc[genus_df_grouped['abundance'] < 1, 'genus'] = 'Other genera <1%'
    genus_df_grouped = genus_df_grouped.groupby(['Barcode', 'genus']).sum().reset_index()
    genus_pivot_table = genus_df_grouped.pivot(index='Barcode', columns='genus', values='abundance').fillna(0)

    # Plot species abundance
    fig_species = go.Figure()
    for column in species_pivot_table.columns:
        fig_species.add_trace(go.Bar(x=species_pivot_table.index, y=species_pivot_table[column], name=column))

    fig_species.update_layout(title='Species Abundance per Barcode',
                               xaxis_title='Barcode',
                               yaxis_title='Abundance (%)',
                               barmode='stack')
    # Save species plot as HTML
    fig_species.write_html(output_species_html)

    # Plot genus abundance
    fig_genus = go.Figure()
    for column in genus_pivot_table.columns:
        fig_genus.add_trace(go.Bar(x=genus_pivot_table.index, y=genus_pivot_table[column], name=column))

    fig_genus.update_layout(title='Genus Abundance per Barcode',
                            xaxis_title='Barcode',
                            yaxis_title='Abundance (%)',
                            barmode='stack')
    # Save genus plot as HTML
    fig_genus.write_html(output_genus_html)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Plot species and genus abundance per barcode")
    parser.add_argument("input_csv", type=str, help="Path to input CSV file")
    parser.add_argument("output_species_html", type=str, help="Path to output HTML file for species plot")
    parser.add_argument("output_genus_html", type=str, help="Path to output HTML file for genus plot")
    args = parser.parse_args()

    # Call plot_abundance function with provided arguments
    plot_abundance(args.input_csv, args.output_species_html, args.output_genus_html)
