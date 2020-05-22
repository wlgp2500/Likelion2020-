---


---

<p><strong>Django를 사용하는 이유</strong></p>
<p>출처 입력</p>
<p>*** Django?**</p>
<ul>
<li>
<p>Python으로 작성하는 웹 프레임워크</p>
</li>
<li>
<p>프론트/백엔드 동시 제공 서버사이드 프레임워크</p>
</li>
<li>
<p>인스타그램도 장고로 개발되었다!</p>
</li>
</ul>
<p><strong>Django 서버 켜기</strong></p>
<p>출처 입력</p>
<p><strong>1. 빈 폴더 ‘prac’ 생성하고 ‘prac’ 안으로 들어가기</strong></p>
<p><strong>2. 가상환경 생성, 활성화</strong></p>
<pre class=" language-javascript"><code class="prism  language-javascript">﻿$ virtualenv myenv
$ source myenv<span class="token operator">/</span>Scripts<span class="token operator">/</span>activate
</code></pre>
<p><strong>3. Django 설치</strong></p>
<pre class=" language-javascript"><code class="prism  language-javascript">$ pip install django

</code></pre>
<p><strong>4. project ‘firstprj’ 생성, 로컬 서버 돌리기</strong></p>
<pre class=" language-javascript"><code class="prism  language-javascript">$ django<span class="token operator">-</span>admin startproject firstprj
$ python manage<span class="token punctuation">.</span>py runserver
</code></pre>
<p><strong>App</strong></p>
<p>출처 입력</p>
<p><strong>1. app 생성하기</strong></p>
<ul>
<li>manage.py로 ‘theapp’ 이라는 이름의 app 생성 실행</li>
</ul>
<pre class=" language-javascript"><code class="prism  language-javascript">$ python manage<span class="token punctuation">.</span>py startapp theapp
</code></pre>
<p><strong>2. firstprj/settings.py 에서 app 등록하기</strong></p>
<ul>
<li>'theapp’추가!</li>
</ul>
<pre class=" language-javascript"><code class="prism  language-javascript">INSTALLED_APPS <span class="token operator">=</span> <span class="token punctuation">[</span>
    <span class="token string">'django.contrib.admin'</span><span class="token punctuation">,</span>
    <span class="token string">'django.contrib.auth'</span><span class="token punctuation">,</span>
    <span class="token string">'django.contrib.contenttypes'</span><span class="token punctuation">,</span>
    <span class="token string">'django.contrib.sessions'</span><span class="token punctuation">,</span>
    <span class="token string">'django.contrib.messages'</span><span class="token punctuation">,</span>
    <span class="token string">'django.contrib.staticfiles'</span><span class="token punctuation">,</span>
    <span class="token string">'theapp'</span><span class="token punctuation">,</span>
<span class="token punctuation">]</span>
</code></pre>
<p><strong>프로젝트 하나 아래에 여러개의 app이 병렬적으로 존재할 수 있다!</strong></p>
<p><strong>Templates</strong></p>
<p>출처 입력</p>
<ol>
<li>Templates 생성</li>
</ol>
<ul>
<li>
<p>theapp/templates 폴더 생성</p>
</li>
<li>
<p>intro.html, main.html, photos.html을 생성한다.</p>
</li>
</ul>
<p><strong>2. <a href="http://views.py">views.py</a></strong></p>
<ul>
<li>
<p>theapp/views.py</p>
</li>
<li>
<p>html 페이지들을 보여주는 함수</p>
</li>
</ul>
<pre class=" language-javascript"><code class="prism  language-javascript"><span class="token keyword">from</span> django<span class="token punctuation">.</span>shortcuts <span class="token keyword">import</span> render

# Create your views here<span class="token punctuation">.</span>
def <span class="token function">main</span><span class="token punctuation">(</span>requests<span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token function">render</span><span class="token punctuation">(</span>requests<span class="token punctuation">,</span> <span class="token string">'main.html'</span><span class="token punctuation">)</span>
def <span class="token function">intro</span><span class="token punctuation">(</span>requests<span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token function">render</span><span class="token punctuation">(</span>requests<span class="token punctuation">,</span><span class="token string">'intro.html'</span><span class="token punctuation">)</span>
def <span class="token function">photos</span><span class="token punctuation">(</span>requests<span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">return</span> <span class="token function">render</span><span class="token punctuation">(</span>requests<span class="token punctuation">,</span><span class="token string">'photos.html'</span><span class="token punctuation">)</span>

</code></pre>
<p><strong>3. <a href="http://ulr.py">ulr.py</a></strong></p>
<ul>
<li>
<p>BASE_DIR/urls.py</p>
</li>
<li>
<p>views.py를 임포트해오고 html 호출하는 url 매핑</p>
</li>
</ul>
<pre class=" language-javascript"><code class="prism  language-javascript"><span class="token keyword">from</span> django<span class="token punctuation">.</span>contrib <span class="token keyword">import</span> admin
<span class="token keyword">from</span> django<span class="token punctuation">.</span>urls <span class="token keyword">import</span> path
<span class="token keyword">from</span> theapp <span class="token keyword">import</span> views

urlpatterns <span class="token operator">=</span> <span class="token punctuation">[</span>
    <span class="token function">path</span><span class="token punctuation">(</span><span class="token string">'admin/'</span><span class="token punctuation">,</span> admin<span class="token punctuation">.</span>site<span class="token punctuation">.</span>urls<span class="token punctuation">)</span><span class="token punctuation">,</span>
    <span class="token function">path</span><span class="token punctuation">(</span><span class="token string">''</span><span class="token punctuation">,</span>views<span class="token punctuation">.</span>main<span class="token punctuation">,</span>name<span class="token operator">=</span><span class="token string">"main"</span><span class="token punctuation">)</span><span class="token punctuation">,</span> #main
    <span class="token function">path</span><span class="token punctuation">(</span><span class="token string">'intro/'</span><span class="token punctuation">,</span>views<span class="token punctuation">.</span>intro<span class="token punctuation">,</span>name<span class="token operator">=</span><span class="token string">"intro"</span><span class="token punctuation">)</span><span class="token punctuation">,</span> #intro
    <span class="token function">path</span><span class="token punctuation">(</span><span class="token string">'gallary/'</span><span class="token punctuation">,</span>views<span class="token punctuation">.</span>photos<span class="token punctuation">,</span>name<span class="token operator">=</span><span class="token string">"photos"</span><span class="token punctuation">)</span><span class="token punctuation">,</span> 

<span class="token punctuation">]</span>

</code></pre>
<p><strong>4. localhost:8000/~</strong></p>
<ul>
<li>
<p>/, /intro/, /gallery/이 urls.py의 path에 정해둔 경로를 통해 요청한다.</p>
</li>
<li>
<p>서버는 해당 html로 응답!</p>
</li>
</ul>
<p><strong>Base Templates</strong></p>
<p>출처 입력</p>
<p>반복되는 html 코드들을 base로 두고 불러오도록!</p>
<p><strong>1. templets/base.html</strong></p>
<ul>
<li>반복되는 코드 적고 **{% block %}**태그로 빈칸 뚫어줌</li>
</ul>
<pre class=" language-javascript"><code class="prism  language-javascript"><span class="token punctuation">{</span><span class="token operator">%</span> block content <span class="token operator">%</span><span class="token punctuation">}</span>
<span class="token punctuation">{</span><span class="token operator">%</span> endblock content <span class="token operator">%</span><span class="token punctuation">}</span>
</code></pre>
<p><strong>2. 각 html에 base.html 확장</strong></p>
<ul>
<li>
<p>각 html 파일 최상단에 <strong>{%extends ‘base.html’%}</strong></p>
</li>
<li>
<p><strong>{%block — %} (개별 코드) {%endblock —%}</strong></p>
</li>
</ul>
<pre class=" language-javascript"><code class="prism  language-javascript"><span class="token punctuation">{</span><span class="token operator">%</span> <span class="token keyword">extends</span> <span class="token string">'base.html'</span> <span class="token operator">%</span><span class="token punctuation">}</span>
<span class="token punctuation">{</span><span class="token operator">%</span> block content<span class="token operator">%</span><span class="token punctuation">}</span>
<span class="token operator">&lt;</span>h1<span class="token operator">&gt;</span>intro<span class="token operator">&lt;</span><span class="token operator">/</span>h1<span class="token operator">&gt;</span>
<span class="token punctuation">{</span><span class="token operator">%</span> endblock content <span class="token operator">%</span><span class="token punctuation">}</span>
</code></pre>

