# Zapisz to jako test_import.py i uruchom
import sys
sys.path.append(r'C:\Studia\SEM I\PBR\EvoDomain')
sys.path.append(r'C:\Studia\SEM I\PBR\EvoDomain\src')
sys.path.append(r'C:\Studia\SEM I\PBR\EvoDomain\src\sut')

# Testowe importowanie
try:
    from src.sut.equation1 import equation1
    print("Import zakończony powodzeniem!")
    print("Wartość equation1(1, 1):", equation1(1, 1))
except Exception as e:
    print(f"Błąd importu: {e}")