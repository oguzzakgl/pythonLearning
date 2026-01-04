import matplotlib.pyplot as plt
import io
import os


def create_spending_pie_chart(summary_df, output_path='spending_pie.png'):
    """
    Özetlenmiş harcama verilerini alır ve bir pasta grafiği oluşturup kaydeder.
    """
    if summary_df.empty:
        return None
    plt.style.use('dark_background') # Koyu tema
    plt.figure(figsize=(3.5, 3.5))
    
    # Pasta grafiği renkleri ve ayarları
    colors = plt.cm.Set3(range(len(summary_df)))
    plt.pie(summary_df['miktar'], labels=summary_df['baslik'], autopct='%1.1f%%', colors=colors)
    
    plt.savefig(output_path, transparent=True, bbox_inches='tight')
    plt.close()
    return output_path
