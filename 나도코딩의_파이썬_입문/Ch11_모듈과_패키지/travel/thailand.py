class ThailandPackage:
    def detail(self):
        print("[태국 3박 5일 패키지] 방콕, 파타야 여행(야시장 투어) 50만원")

if __name__ == "__main__":
    print("thailand 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 출력")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("외부에서 thailand 모듈 호출")