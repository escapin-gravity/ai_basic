<div style="max-width: 800px; margin: 0 auto;">
  <h1 style="font-size: 2.5em; font-weight: bold; margin-bottom: 20px; text-align: left;">🚀 Torch Basic</h1>

  <h3 style="font-size: 1.3em; margin-bottom: 10px; text-align: left;">📖 Overview</h3>
  <p style="line-height: 1.6; color: #444; text-align: left;">
    <b>AI Basic</b> 레포지토리는 PyTorch를 기반으로 인공지능과 딥러닝의 핵심 개념 및 구현을 학습하기 위한 프로젝트입니다. 단계별 학습 자료와 실습 예제들을 통해 기초부터 고급 주제까지 다룹니다.
  </p>

  <hr style="border: 1px solid #D0D0D0; margin: 20px 0;">

  <h3 style="font-size: 1.3em; margin-bottom: 10px; text-align: left;">🧠 Topics Covered</h3>
  <p style="margin-bottom: 15px; text-align: left;">다음은 레포지토리에서 다루는 주요 주제들입니다:</p>

  <div style="margin-left: 20px;">
    <ul style="line-height: 1.7; margin-bottom: 20px; text-align: left;">
      <li><b>PyTorch Basics</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>텐서 생성 및 조작</li>
          <li>데이터 로딩 및 전처리</li>
        </ul>
      </li>
      <li><b>Autograd (자동미분)</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>자동 미분 메커니즘 이해</li>
          <li>그래디언트 계산</li>
        </ul>
      </li>
      <li><b>Gradient Descent (경사하강법)</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>손실 함수 정의</li>
          <li>모델 파라미터 최적화</li>
        </ul>
      </li>
      <li><b>Optimization (최적화)</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>다양한 최적화 알고리즘 (SGD, Adam, RMSprop 등)</li>
        </ul>
      </li>
      <li><b>Regression (회귀)</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>선형 회귀, 다항 회귀 구현</li>
          <li>모델 훈련 및 평가</li>
        </ul>
      </li>
      <li><b>Custom Models</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>사용자 정의 모델 구성</li>
          <li>PyTorch 클래스 활용</li>
        </ul>
      </li>
      <li><b>Deep Neural Networks (DNN)</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>다층 신경망 설계</li>
          <li>활성화 함수 적용 및 최적화</li>
        </ul>
      </li>
       <li><b>Initialization / Batch Norm / Dropout</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>가중치 초기화</li>
          <li>배치 정규화 및 드롭아웃 활용</li>
        </ul>
       </li>
      <li><b>Convolutional Neural Networks (CNN)</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>합성곱 신경망 구조 및 이미지 데이터 처리</li>
        </ul>
      </li>
      <li><b>Autoencoders</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>데이터 압축 및 복원</li>
          <li>딥러닝 기반 특성 학습</li>
        </ul>
      </li>
      <li><b>Generative Adversarial Networks (GAN)</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>Generator와 Discriminator 구조</li>
          <li>생성 모델 학습</li>
        </ul>
      </li>
      <li><b>Recurrent Neural Networks (RNN, LSTM, GRU)</b>
        <ul style="list-style-type: square; margin-left: 20px;">
          <li>순차 및 시계열 데이터 처리</li>
          <li>다양한 RNN 아키텍처 적용</li>
        </ul>
      </li>
      <li><b>Pre-trained Models</b>
        <ul style="list-style-type: square; margin-left: 20px;">
            <li>사전학습 모델 활용 (Transfer Learning)</li>
            <li>Fine-tuning을 통한 적응 학습</li>
         </ul>
      </li>
        <li><b>Early Stopping</b>
        <ul style="list-style-type: square; margin-left: 20px;">
             <li>과적합 방지를 위한 조기 종료 전략</li>
        </ul>
      </li>
      <li><b>Tensor Models</b>
        <ul style="list-style-type: square; margin-left: 20px;">
             <li>텐서를 활용한 고성능 모델 설계</li>
         </ul>
      </li>
    </ul>
  </div>

  <hr style="border: 1px solid #D0D0D0; margin: 20px 0;">

  <h3 style="font-size: 1.3em; margin-bottom: 10px; text-align: left;">📂 Repository Structure</h3>
  <pre style="background-color: #F8F8F8; padding: 15px; border: 1px solid #E0E0E0; border-radius: 5px; overflow-x: auto; font-size: 14px; text-align: left;">
ai_basic/
├── 01_pytorch_basics/       # PyTorch 기초
├── 02_autograd/             # 자동미분
├── 03_gradient_descent/     # 경사하강법
├── 04_optimization/         # 최적화
├── 05_regression/           # 회귀
├── 06_custom_models/        # 사용자 정의 모델
├── 07_dnn/                  # 다층 신경망
├── 08_initialization_bn_do/ # 초기화, 배치 정규화, 드롭아웃
├── 09_cnn/                  # 합성곱 신경망
├── 10_autoencoder/          # 오토인코더
├── 11_gan/                  # GAN
├── 12_rnn_lstm_gru/         # 순환 신경망
├── 13_pretrained_models/    # 사전학습 모델
├── 14_early_stopping/       # 조기 종료
├── 15_tensor_models/        # 텐서 모델
└── README.md
  </pre>
</div>
