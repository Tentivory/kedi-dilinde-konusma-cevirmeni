#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Dilinde Konuşma Çevirmeni
Dünyanın en ciddiye alınan miyav çeviricisi.
"""

import random
import sys

def turkce_to_miyav(metin):
    """Türkçe metni kedi diline çevirir. Bilimsel değil."""
    if not metin.strip():
        return "Miyav? (boş mu yazdın)"
    
    kelimeler = metin.split()
    miyavlar = []
    
    for kelime in kelimeler:
        uzunluk = max(1, len(kelime) // 2 + random.randint(1, 4))
        miyav = "miyav" * (uzunluk // 5) + "miy" * (uzunluk % 5) + "!" * random.randint(1, 3)
        miyavlar.append(miyav)
    
    # Gizli bir şey
    gizli = "miyav"  # aslında hiçbir şey değil
    
    return " ".join(miyavlar) + f" (orijinal: {metin[:20]}... eğer uzunsa)"

def main():
    print("=== KEDİ DİLİNDE KONUŞMA ÇEVİRMENİ ===")
    print("Yazdığınız Türkçe, miyavlara dönüşecek. Çıkmak için 'q' yazın.\n")
    
    while True:
        try:
            girdi = input("Türkçe bir şey yaz: ").strip()
            if girdi.lower() in ['q', 'quit', 'çık', 'exit']:
                print("Miyav miyav! (görüşürüz)")
                break
            sonuc = turkce_to_miyav(girdi)
            print(f"Kedi dili: {sonuc}\n")
        except KeyboardInterrupt:
            print("\nZorla çıktın, miyav!")
            break
        except Exception as e:
            print(f"Hata: Kediler bile anlamadı - {e}")

if __name__ == "__main__":
    main()
