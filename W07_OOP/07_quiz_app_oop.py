# Konu: Quiz Uygulaması (OOP)
# Amaç: OOP prensiplerini kullanarak soru, cevap ve skor takibi yapan bir Quiz uygulaması geliştirmek.

# 1. Sınıfları Tanımlama
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        # Cevap kontrolünü daha güvenli hale getirelim (örn: 'c' vs 'C')
        return answer.upper() == self.answer.upper()

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def get_question(self):
        # Mevcut soru indeksindeki soruyu döndürür
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        # Bu metot SADECE soruyu gösterir. Başka bir metodu ÇAĞIRMAZ.
        question = self.get_question()
        
        print(f"\n--- Soru {self.questionIndex + 1} ---")
        print(question.text)

        for choice in question.choices:
            print(choice)
    
    def guess(self, answer):
        # Bu metot SADECE cevabı işler. Skoru ve indeksi günceller.
        question = self.get_question()
        
        if question.check_answer(answer):
            self.score += 1
            print("✨ Doğru Cevap!")
        else:
            print(f"😔 Yanlış Cevap. Doğru cevap: {question.answer}")
            
        # Bir sonraki soruya geçmek için indeksi artır
        self.questionIndex += 1

    def has_more_questions(self):
        # Quiz'in bitip bitmediğini kontrol eden yardımcı metot
        return self.questionIndex < len(self.questions)

    def showScore(self):
        # Quiz bittiğinde skoru gösterir
        print("\n--- QUIZ BİTTİ ---")
        print(f"Toplam {len(self.questions)} sorudan {self.score} tanesini doğru bildiniz.")
        print(f"Başarı yüzdeniz: { (self.score / len(self.questions)) * 100 }%")


# 2. Soruları Oluşturma
q1 = Question(
    "What is the capital of France?", 
    ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
    "C"
)
q2 = Question(
    "What is the capital of Turkey?",
    ["A) Istanbul", "B) Ankara", "C) Izmir", "D) Bursa"],
    "B"
)
q3 = Question(
    "Which programming language is this quiz written in?",
    ["A) Java", "B) C#", "C) Python", "D) JavaScript"],
    "C"
)

# Soru listesi
liste = [q1, q2, q3]

# 3. Quiz Nesnesini Oluşturma
quiz = Quiz(liste)

# 4. Ana Quiz Döngüsü
# Bu döngü, quiz'i başından sonuna kadar çalıştıran ana motordur.
print("🎉 Quiz Başlıyor! 🎉")

while quiz.has_more_questions():
    # 1. Soruyu göster
    quiz.displayQuestion()
    
    # 2. Kullanıcıdan cevabı al
    answer = input("Cevabınız (A, B, C veya D): ")
    
    # 3. Cevabı işle (kontrol et, skoru ve indeksi güncelle)
    quiz.guess(answer)

# 5. Döngü bittiğinde (sorular bittiğinde) final skorunu göster
quiz.showScore()