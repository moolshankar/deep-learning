import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterVisitorComponent } from './register-visitor.component';

describe('RegisterVisitorComponent', () => {
  let component: RegisterVisitorComponent;
  let fixture: ComponentFixture<RegisterVisitorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegisterVisitorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegisterVisitorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
