const steps = [
    {
        num: "STEP 01",
        title: "G Portal 화면에서 일정 등록",
        desc: "회의를 시작하기 위해 우선 G Portal의 캘린더 메뉴에서 회의 일정을 등록해 주세요.",
        caution: "참석자 명단이 정확해야 회의록 공유가 원활하게 진행됩니다.",
        img: "assets/images/step1.png"
    },
    {
        num: "STEP 02",
        title: "Webex 선택 및 AI 회의록 옵션 선택",
        desc: "일정 작성 화면에서 화상회의 도구로 'Webex'를 선택하고, 하단의 'AI 회의록 사용' 옵션을 체크해 주세요.",
        caution: "이 옵션을 켜야만 녹음 및 요약 기능이 활성화됩니다.",
        img: "assets/images/step2.png"
    },
    {
        num: "STEP 03",
        title: "예약한 시간에 웨벡스 접속",
        desc: "회의 시간이 되면 G Portal 알림 또는 링크를 통해 생성된 Webex 회의방에 입장합니다.",
        caution: "주최자가 입장해야 AI 기능이 정상적으로 시작됩니다.",
        img: "assets/images/step3.png"
    },
    {
        num: "STEP 04",
        title: "녹음 고지 동의 (개인정보보호)",
        desc: "입장 시 'AI 회의록 작성을 위한 녹음/녹화가 진행됩니다'라는 안내 팝업이 뜹니다. 반드시 '동의'를 눌러주세요.",
        caution: "거절 시 마이크가 자동으로 음소거(Mute) 처리되어 회의 참여에 제한이 있을 수 있습니다.",
        img: "assets/images/step4.png"
    },
    {
        num: "STEP 05",
        title: "회의 종료",
        desc: "회의가 끝나면 Webex 종료 버튼을 눌러 퇴장합니다. AI가 즉시 데이터 처리를 시작합니다.",
        caution: "비정상 종료 시 데이터 처리에 시간이 더 소요될 수 있습니다.",
        img: "assets/images/step5.png"
    },
    {
        num: "STEP 06",
        title: "회의록 및 첨부파일 확인",
        desc: "회의 종료 후 약 5~10분 뒤, G Portal 일정의 '회의록' 탭에서 생성된 텍스트 기록과 요약 파일을 확인할 수 있습니다.",
        caution: "대외비 내용이 포함된 경우 공유 범위 설정에 주의해 주세요.",
        img: "assets/images/step6.png"
    }
];

let currentStep = 0;

function updateStep() {
    const step = steps[currentStep];
    const imgEl = document.getElementById('step-img');
    const numEl = document.getElementById('step-num');
    const titleEl = document.getElementById('step-title');
    const descEl = document.getElementById('step-desc');
    const cautionEl = document.getElementById('step-caution');
    
    // Animate transition
    imgEl.parentElement.style.opacity = '0';
    setTimeout(() => {
        imgEl.src = step.img;
        numEl.innerText = step.num;
        titleEl.innerText = step.title;
        descEl.innerText = step.desc;
        cautionEl.innerHTML = `<strong>⚠️ 주의사항:</strong> ${step.caution}`;
        imgEl.parentElement.style.opacity = '1';
    }, 300);

    // Update buttons
    document.getElementById('prev-btn').disabled = currentStep === 0;
    document.getElementById('next-btn').innerText = currentStep === steps.length - 1 ? '처음으로' : '다음';

    // Update dots
    updateDots();
}

function changeStep(delta) {
    currentStep += delta;
    if (currentStep >= steps.length) currentStep = 0;
    if (currentStep < 0) currentStep = 0;
    updateStep();
}

function updateDots() {
    const dotsContainer = document.getElementById('dots');
    dotsContainer.innerHTML = '';
    steps.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.className = `dot ${index === currentStep ? 'active' : ''}`;
        dotsContainer.appendChild(dot);
    });
}

function switchSection(sectionId) {
    // Update nav buttons
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.innerText.includes(sectionId === 'meeting-minutes' ? '회의록' : sectionId === 'translation' ? '통번역' : '모바일')) {
            item.classList.add('active');
        }
    });

    // Show selected section
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.remove('active');
    });
    document.getElementById(sectionId).classList.add('active');
    
    // Reset step if it's the first section
    if (sectionId === 'meeting-minutes') {
        currentStep = 0;
        updateStep();
    }
}

// Initial Load
document.addEventListener('DOMContentLoaded', () => {
    updateStep();
});
